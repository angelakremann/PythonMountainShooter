import pygame

# Inicializa o Pygame
pygame.init()

# Define o título da janela

pygame.display.set_caption("Pygame a partir de Victor Borin - Angela Kretschmann")

# O restante do código de inicialização do jogo
from code.Game import Game

game = Game()

game.run()


