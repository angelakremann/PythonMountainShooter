from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Player import Player
from code.PlayerShot import PlayerShot

class EntityMediator:
    @staticmethod
    def __verify_collision_window(ent: Entity):
        # Remove entidades se saírem da tela
        if isinstance(ent, Enemy) and ent.rect.right <= 0:
            ent.health = 0
        elif isinstance(ent, PlayerShot) and ent.rect.left >= WIN_WIDTH:
            ent.health = 0
        elif isinstance(ent, EnemyShot) and ent.rect.right <= 0:
            ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        # Verifica colisão e aplica dano entre diferentes tipos de entidades
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            if ent1.rect.colliderect(ent2.rect):
                ent1.health -= ent2.damage
                ent2.health = 0  # Tiro é removido ao colidir
                ent1.last_dmg = ent2.name

        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            if ent1.rect.colliderect(ent2.rect):
                ent2.health -= ent1.damage
                ent1.health = 0
                ent2.last_dmg = ent1.name

        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            if ent1.rect.colliderect(ent2.rect):
                ent1.health -= ent2.damage
                ent2.health = 0

        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            if ent1.rect.colliderect(ent2.rect):
                ent2.health -= ent1.damage
                ent1.health = 0

        elif isinstance(ent1, Player) and isinstance(ent2, Enemy):
            if ent1.rect.colliderect(ent2.rect):
                ent1.health -= 10  # Dano ao jogador ao tocar o inimigo
                ent2.health = 0  # Inimigo é removido ao colidir com o jogador

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        # Atualiza o score do jogador ao destruir um inimigo
        if enemy.last_dmg == 'Player1Shot':
            for ent in entity_list:
                if ent.name == 'Player1':
                    ent.score += enemy.score
                    print(f"{ent.name} score atualizado para {ent.score}")
        elif enemy.last_dmg == 'Player2Shot':
            for ent in entity_list:
                if ent.name == 'Player2':
                    ent.score += enemy.score
                    print(f"{ent.name} score atualizado para {ent.score}")

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        # Verifica colisões entre entidades e com a janela
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        # Remove entidades com saúde zero ou negativa
        for ent in entity_list[:]:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)
                entity_list.remove(ent)
