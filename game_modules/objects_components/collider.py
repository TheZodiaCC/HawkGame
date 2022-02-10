from core.core_consts import WorldConsts
import pygame as pg


class Collider:
    def __init__(self, center, w, h):
        self.center = center

        self.render_w = w
        self.render_h = h

        self.world_w = self.render_w / WorldConsts.WORLD_SIZE_TO_PIXELS_FACTOR
        self.world_h = self.render_h / WorldConsts.WORLD_SIZE_TO_PIXELS_FACTOR

        self.rect = None

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

    def setup_center(self, center):
        self.center = center

        self.rect = pg.Rect(self.center[0], self.center[1], self.world_w, self.world_h)
