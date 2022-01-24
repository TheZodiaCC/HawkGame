from game_modules.entities.entity_base import EntityBase
import os
import pygame as pg


class Player(EntityBase):
    def __init__(self):
        super().__init__()

        self.model = None
        self.rect = None
        self.position = [0, 0]

        self.init_entity_model()

    def init_entity_model(self):
        self.model = pg.image.load(os.path.join(os.path.join("graphic", "player"), "player.png"))
        self.model = pg.transform.scale(self.model, (50, 50))

        self.rect = self.model.get_rect()

        self.position = [self.position[0] - self.model.get_width() / 2, self.position[1] - self.model.get_height() / 2]
