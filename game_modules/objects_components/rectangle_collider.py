from game_modules.objects_components.collider_base import ColliderBase


class RectangleCollider(ColliderBase):
    def __init__(self, center, w, h):
        super().__init__(center=center, w=w, h=h)

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
