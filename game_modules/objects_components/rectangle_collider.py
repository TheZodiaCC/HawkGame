from game_modules.objects_components.collider_base import ColliderBase


class RectangleCollider(ColliderBase):
    def __init__(self, center, w, h):
        super().__init__(center=center, w=w, h=h)
