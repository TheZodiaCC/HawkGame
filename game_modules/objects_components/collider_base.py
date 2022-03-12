from core.core_consts import WorldConsts
import pygame as pg


class ColliderBase:
    def __init__(self, center, radius=None, w=None, h=None):
        self.center = center
        self.radius = radius

        self.render_w = w
        self.render_h = h

        self.world_w = None
        self.world_h = None

    def update(self, world_position):
        self.center = world_position

    def init(self):
        if self.render_w is not None and self.render_h is not None:
            self.init_rectangle_collider()

        elif self.radius is not None:
            self.init_circle_collider()

    def init_rectangle_collider(self):
        self.world_w = self.render_w / WorldConsts.WORLD_SIZE_TO_PIXELS_FACTOR
        self.world_h = self.render_h / WorldConsts.WORLD_SIZE_TO_PIXELS_FACTOR

        self.rect = pg.Rect(self.center[0], self.center[1], self.world_w, self.world_h)

    def init_circle_collider(self):
        pass
