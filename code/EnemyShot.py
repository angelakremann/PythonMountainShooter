from code.Const import ENTITY_SPEED
from code.Entity import Entity

class EnemyShot(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        # Move o tiro para a esquerda, em direção ao jogador
        self.rect.centerx -= ENTITY_SPEED.get(self.name, 5)  # Velocidade padrão caso não esteja definida

        # Remover o tiro se ele sair da tela pela esquerda
        if self.rect.right < 0:
            self.health = 0  # Marca para remoção ao sair da tela
            return True
        return False

