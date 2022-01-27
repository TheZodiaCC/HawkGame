from game_modules.entities.entity_base import EntityBase
from game_modules.entities.consts import PlayerConsts
from core.render.render_object import RenderObject


class TestSphere(EntityBase):
    def __init__(self):
        super().__init__()

        self.position = [550, 550]
        self.render_object = RenderObject(self, PlayerConsts.PLAYER_MODEL_PATH, PlayerConsts.PLAYER_MODEL_SIZE)
