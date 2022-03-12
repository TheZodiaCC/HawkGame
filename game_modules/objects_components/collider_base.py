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

        self.rect = None

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

    def get_render_xyxy(self):
        x1 = self.center[0] - self.render_w / 2
        y1 = self.center[1] - self.render_h / 2
        x2 = self.center[0] + self.render_w / 2
        y2 = self.center[1] + self.render_h / 2

        return [x1, y1, x2, y2]

    def get_world_xyxy(self):
        x1 = self.center[0] - self.world_w / 2
        y1 = self.center[1] - self.world_h / 2
        x2 = self.center[0] + self.world_w / 2
        y2 = self.center[1] + self.world_h / 2

        return [x1, y1, x2, y2]

    def get_render_xywh(self):
        x1 = self.center[0] - self.render_w / 2
        y1 = self.center[1] - self.render_h / 2

        return [x1, y1, self.render_w, self.render_h]

    def get_world_xywh(self):
        x1 = self.center[0] - self.world_w / 2
        y1 = self.center[1] - self.world_h / 2

        return [x1, y1, self.world_w, self.world_h]
