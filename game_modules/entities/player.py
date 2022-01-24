from game_modules.entities.entity_base import EntityBase
from core.utils import vectors_utils
import os
import pygame as pg


class Player(EntityBase):
    def __init__(self):
        super().__init__()

        self.model = None
        self.rect = None
        self.position = [0, 0]

        self.init_player_model()

        self.orientation_diff = 0

    def init_player_model(self):
        self.model = pg.image.load(os.path.join(os.path.join("graphic", "player"), "player.png"))
        self.model = pg.transform.scale(self.model, (50, 50))

        self.rect = self.model.get_rect()

        self.position = [self.position[0] - self.model.get_width() / 2, self.position[1] - self.model.get_height() / 2]

    def get_position(self):
        return self.position

    def set_orientation(self, dest_vector):
        self.orientation_diff = vectors_utils.get_degrees_between_vectors(dest_vector, self.get_position())
