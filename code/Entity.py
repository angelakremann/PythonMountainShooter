#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
import pygame.image
from code.Const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE, ENTITY_SPEED, ENTITY_SHOT_DELAY

class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = ENTITY_SPEED.get(self.name, 0)  # Define a velocidade com valor padrão de 0
        self.health = ENTITY_HEALTH.get(self.name, 0)  # Define a saúde com valor padrão de 0
        self.damage = ENTITY_DAMAGE.get(self.name, 0)  # Define o dano com valor padrão de 0
        self.score = ENTITY_SCORE.get(self.name, 0)    # Define a pontuação com valor padrão de 0
        self.last_dmg = 'None'

    @abstractmethod
    def move(self):
        pass

# Definindo a classe Enemy3 que herda de Entity
class Enemy3(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY.get(self.name, 0)  # Define o atraso de tiro com valor padrão de 0

    def move(self):
        # Movimentação específica do Enemy3
        self.rect.centerx -= ENTITY_SPEED.get(self.name, 1)  # Usa um valor padrão de velocidade de 1 para Enemy3

    def shoot(self):
        # Importa EnemyShot apenas quando necessário para evitar ciclos de importação
        from code.EnemyShot import EnemyShot
        return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
