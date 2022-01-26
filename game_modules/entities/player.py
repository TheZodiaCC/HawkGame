from game_modules.entities.entity_base import EntityBase
from game_modules.entities.consts import PlayerConsts
from core.render.render_object import RenderObject


class Player(EntityBase):
    def __init__(self):
        super().__init__()

        self.render_object = RenderObject(self, PlayerConsts.PLAYER_MODEL_PATH, PlayerConsts.PLAYER_MODEL_SIZE, True,
                                          PlayerConsts.PLAYER_MODEL_ORIGIN_POINT)
        self.position = [5000, 5000]
