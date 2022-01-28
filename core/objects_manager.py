from game_modules.entities.player import Player


class ObjectsManager:
    def __init__(self):
        self.player = None

        self.game_objects = []

    def init_player(self):
        self.player = Player()

        self.game_objects.append(self.player)

    def add_game_object(self, obj):
        self.game_objects.append(obj)
