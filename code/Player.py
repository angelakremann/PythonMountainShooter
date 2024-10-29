import pygame
from code.Const import ENTITY_SPEED, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, ENTITY_SHOT_DELAY
from code.Entity import Entity
from code.PlayerShot import PlayerShot

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = 0  # Inicializando com zero para permitir o primeiro disparo imediato

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < pygame.display.get_surface().get_height():
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < pygame.display.get_surface().get_width():
            self.rect.centerx += ENTITY_SPEED[self.name]

    def shoot(self):
        if self.shot_delay <= 0:
            pressed_key = pygame.key.get_pressed()
            if pressed_key[pygame.K_LCTRL]:  # Tecla Ctrl esquerda para disparar
                self.shot_delay = ENTITY_SHOT_DELAY.get(self.name, 5)  # Reinicia o atraso do tiro para 5 frames
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.top))
        else:
            self.shot_delay -= 1
        return None
