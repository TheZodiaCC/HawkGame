import pygame as pg
from core.utils import path_utils


class RenderObject:
    def __init__(self, model_path, model_size, freezed=False, origin=None):
        self.freezed = freezed
        self.origin = origin

        self.position = [0, 0]
        self.model = None
        self.rect = None

        self.model_path = model_path
        self.model_size = model_size

        self.init_model()

    def init_model(self):
        self.model = pg.image.load(path_utils.get_abs_path(self.model_path))
        self.model = pg.transform.scale(self.model, self.model_size)

        self.rect = self.model.get_rect()

        if self.freezed:
            self.position = self.origin

        self.position = [self.position[0], self.position[1]]
