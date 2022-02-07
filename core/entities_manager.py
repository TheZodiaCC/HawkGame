from game_modules.entities.player import Player
from game_modules.entities.test_sphere import TestSphere


class EntitiesManager:
    def __init__(self):
        self.player = None

        self.entities = []

    def init_player(self):
        self.player = Player()

        self.entities.append(self.player)

    def add_entity(self, obj):
        self.entities.append(obj)

    def add_debug_entity(self):
        debug_sphere = TestSphere()
        debug_sphere.position = [530, 530]

        self.add_entity(debug_sphere)
