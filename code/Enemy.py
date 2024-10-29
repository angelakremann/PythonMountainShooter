from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.Entity import Entity
from code.EnemyShot import EnemyShot

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY.get(self.name, 10)  # Valor reduzido para disparos rápidos

    def move(self):
        self.rect.centerx -= ENTITY_SPEED.get(self.name, 1)

    def shoot(self):
        if self.shot_delay <= 0:
            self.shot_delay = ENTITY_SHOT_DELAY.get(self.name, 10)  # Reinicia o atraso do tiro
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
        else:
            self.shot_delay -= 1
        return None


class Enemy3(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY.get(self.name, 5)
        self.moving_down = True

    def move(self):
        self.rect.centerx -= ENTITY_SPEED.get(self.name, 1)

        if self.moving_down:
            self.rect.centery += ENTITY_SPEED.get(self.name, 1)
            if self.rect.bottom >= WIN_HEIGHT:
                self.moving_down = False
        else:
            self.rect.centery -= ENTITY_SPEED.get(self.name, 1) * 2
            if self.rect.top <= 0:
                self.moving_down = True

    def shoot(self):
        if self.shot_delay <= 0:
            self.shot_delay = ENTITY_SHOT_DELAY.get(self.name, 5)
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
        else:
            self.shot_delay -= 1
        return None
