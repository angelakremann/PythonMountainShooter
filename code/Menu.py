#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import sys  # Importação do módulo sys
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import WIN_WIDTH, C_ORANGE, MENU_OPTION, C_WHITE, C_YELLOW, WIN_HEIGHT


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            # Desenha o fundo e o texto do menu
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Mountain", C_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", C_ORANGE, ((WIN_WIDTH / 2), 120))
            # Adicionando o nome no canto inferior direito
            self.menu_text(15, '4110110 Angela Kretschmann', C_WHITE, (WIN_WIDTH - 150, WIN_HEIGHT - 30))

            # Opções do menu
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], C_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))
            pygame.display.flip()

            # Eventos do menu
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer_music.stop()
                    pygame.quit()
                    sys.exit()  # Encerra o sistema de forma limpa

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        menu_option = (menu_option + 1) % len(MENU_OPTION)
                    elif event.key == pygame.K_UP:
                        menu_option = (menu_option - 1) % len(MENU_OPTION)
                    elif event.key == pygame.K_RETURN:
                        pygame.mixer_music.stop()
                        return MENU_OPTION[menu_option]  # Retorna a opção selecionada

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.SysFont("Arial", text_size)  # Fonte ajustada para Arial
        text_surf = text_font.render(text, True, text_color)
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)
