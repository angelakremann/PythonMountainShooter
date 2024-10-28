from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.Entity import Entity
from code.EnemyShot import EnemyShot

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY.get(self.name, 0)

    def move(self):
        # Movimento padrão da direita para a esquerda
        self.rect.centerx -= ENTITY_SPEED.get(self.name, 1)

    def shoot(self):
        return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))

class Enemy3(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY.get(self.name, 0)
        self.moving_down = True  # Começa movendo-se para baixo

    def move(self):
        # Movimento horizontal para a esquerda
        self.rect.centerx -= ENTITY_SPEED.get(self.name, 1)

        # Movimento vertical alternado para Enemy3
        if self.moving_down:
            self.rect.centery += ENTITY_SPEED.get(self.name, 1)
            if self.rect.bottom >= WIN_HEIGHT:
                self.moving_down = False
        else:
            self.rect.centery -= ENTITY_SPEED.get(self.name, 1) * 2
            if self.rect.top <= 0:
                self.moving_down = True

    def shoot(self):
        return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
