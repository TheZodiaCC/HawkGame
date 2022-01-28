from game_modules.entities.player import Player
from game_modules.entities.test_sphere import TestSphere


class ObjectsManager:
    def __init__(self):
        self.player = None

        self.game_objects = []

    def init_player(self):
        self.player = Player()

        self.game_objects.append(self.player)

    def add_game_object(self, obj):
        self.game_objects.append(obj)

    def add_debug_object(self):
        debug_sphere = TestSphere()
        debug_sphere.position = [530, 530]

        self.add_game_object(debug_sphere)
