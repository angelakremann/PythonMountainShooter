import random
import sys
import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import (
    C_WHITE, WIN_HEIGHT, WIN_WIDTH, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME,
    C_GREEN, C_CYAN, EVENT_TIMEOUT, TIMEOUT_STEP, TIMEOUT_LEVEL,
    ENTITY_SPEED, ENTITY_SHOT_DELAY
)
from code.Enemy import Enemy, Enemy3
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player

class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list = EntityFactory.get_entity(self.name + 'Bg') + [EntityFactory.get_entity('Player1')]
        self.timeout = TIMEOUT_LEVEL  # Tempo padrão, ajustável para cada fase
        self.player_score = player_score

        # Define o tipo de inimigo com base na fase atual
        self.enemy_type = {'Level1': 'Enemy1', 'Level2': 'Enemy2', 'Level3': 'Enemy3'}.get(name)

        # Ajuste do tempo para cada fase
        if name == 'Level1':
            self.timeout = 10000  # 10 segundos para a Fase 1
        elif name == 'Level2':
            self.timeout = 10000  # 10 segundos para a Fase 2
        elif name == 'Level3':
            self.timeout = 20000  # 20 segundos para a Fase 3

        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)


    def run(self, player_score):
        # Carregar e tocar música da fase
        try:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(f'./asset/{self.name}.mp3')
            pygame.mixer.music.set_volume(0.3)
            pygame.mixer.music.play(-1)
            print(f"Tocando música: {self.name}.mp3")
        except Exception as e:
            print(f"Erro ao carregar a música: {e}")

        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            self.window.fill((0, 0, 0))

            # Atualiza e desenha o fundo
            for bg in [e for e in self.entity_list if e.name.startswith(self.name + 'Bg')]:
                bg.move()
                self.window.blit(bg.surf, bg.rect)

            # Atualiza e desenha outras entidades
            for ent in self.entity_list[:]:
                ent.move()
                self.window.blit(ent.surf, ent.rect)

                # Controle de disparo do jogador
                if isinstance(ent, Player):
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_LCTRL]:  # Pressiona Ctrl para disparar
                        shoot = ent.shoot()
                        if shoot:
                            self.entity_list.append(shoot)

                # Disparo dos inimigos com controle de atraso
                if isinstance(ent, (Enemy, Enemy3)):
                    if ent.shot_delay <= 0:
                        shoot = ent.shoot()
                        if shoot:
                            self.entity_list.append(shoot)
                        ent.shot_delay = ENTITY_SHOT_DELAY.get(ent.name, 0)  # Redefine o atraso de disparo
                    else:
                        ent.shot_delay -= 1  # Reduz o atraso do tiro a cada frame

            # Processa os eventos do jogo
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    # Entrada de inimigos específicos para a fase
                    enemy = EntityFactory.get_entity(self.enemy_type)
                    if enemy:
                        self.entity_list.append(enemy)
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout <= 0:
                        # Garante que o jogador esteja na lista antes de acessar `score`
                        player_entity = next((ent for ent in self.entity_list if isinstance(ent, Player)), None)
                        if player_entity:
                            # Acumula o score ao final da fase
                            player_score[0] += player_entity.score
                        return True

            # Exibe o HUD
            self.display_hud(clock)

            # Atualiza colisões e vida das entidades
            EntityMediator.verify_collision(self.entity_list)
            EntityMediator.verify_health(self.entity_list)
            pygame.display.flip()

    def display_hud(self, clock):
        # Exibe cronômetro e FPS no HUD
        self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', C_WHITE, (10, 5))
        self.level_text(14, f'fps: {clock.get_fps():.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
        self.level_text(14, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font = pygame.font.SysFont("Arial", text_size)
        text_surf = text_font.render(text, True, text_color)
        text_rect = text_surf.get_rect(topleft=text_pos)
        self.window.blit(text_surf, text_rect)
