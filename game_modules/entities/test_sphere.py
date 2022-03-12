from game_modules.entities.entity_base import EntityBase
from game_modules.entities.entities_consts import PlayerConsts
from core.render.render_object import RenderObject
from game_modules.objects_components.rectangle_collider import RectangleCollider


class TestSphere(EntityBase):
    def __init__(self):
        super().__init__()

        self.position = [0, 0]
        self.render_object = RenderObject(self, PlayerConsts.MODEL_PATH, PlayerConsts.MODEL_SIZE)

        self.collider = RectangleCollider(self.position, PlayerConsts.MODEL_SIZE[0], PlayerConsts.MODEL_SIZE[1])
