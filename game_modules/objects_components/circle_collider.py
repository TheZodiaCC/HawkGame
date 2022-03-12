from game_modules.objects_components.collider_base import ColliderBase


class CircleCollider(ColliderBase):
    def __init__(self, center, radius):
        super().__init__(center=center, radius=radius)
