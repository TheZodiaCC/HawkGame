from core.core_consts import WorldConsts


class Collider:
    def __init__(self, center, w, h):
        self.center = center
        self.w = w / WorldConsts.WORLD_SIZE_TO_PIXELS_FACTOR
        self.h = h / WorldConsts.WORLD_SIZE_TO_PIXELS_FACTOR

    def get_xyxy(self):
        x1 = self.center[0] - self.w / 2
        y1 = self.center[1] - self.h / 2
        x2 = self.center[0] + self.w / 2
        y2 = self.center[1] + self.h / 2

        return [x1, y1, x2, y2]

    def get_xywh(self):
        x1 = self.center[0] - self.w / 2
        y1 = self.center[1] - self.h / 2

        return [x1, y1, self.w, self.h]

    def setup_center(self, center):
        self.center = center
