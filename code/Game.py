import sys
import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu
from code.Score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Mountain Shooter")

    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0, 0]  # [Player1, Player2]

                # Fase 1
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)

                # Fase 2
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)

                # Fase 3 e exibição do score ao final
                if level_return:
                    level = Level(self.window, 'Level3', menu_return, player_score)
                    level_return = level.run(player_score)

                    if level_return:
                        score.save(menu_return, player_score)
                        score.show()  # Exibir o score final

            elif menu_return == MENU_OPTION[3]:  # Opção para ver o score
                score.show()
            elif menu_return == MENU_OPTION[4]:  # Opção para sair do jogo
                pygame.quit()
                sys.exit()  # Finaliza o sistema de forma segura
            else:
                pygame.quit()
                sys.exit()  # Finaliza o sistema de forma segura


if __name__ == "__main__":
    game = Game()
    game.run()
