from game_modules.entities.player import Player
from game_modules.controllers.player_controller import PlayerController


class ObjectsManager:
    def __init__(self):
        self.player = None
        self.player_controller = None

        self.game_objects = []

    def init_player(self):
        self.player = Player()
        self.player_controller = PlayerController(self.player)

        self.game_objects.append(self.player)

    def add_game_object(self, obj):
        self.game_objects.append(obj)
