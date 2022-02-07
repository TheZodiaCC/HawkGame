from game_modules.entities.entity_base import EntityBase
from game_modules.entities.entities_consts import PlayerConsts
from core.render.render_object import RenderObject


class Player(EntityBase):
    def __init__(self):
        super().__init__()

        self.position = [500, 500]
        self.fov = PlayerConsts.PLAYER_FOV
        self.render_object = RenderObject(self, PlayerConsts.PLAYER_MODEL_PATH, PlayerConsts.PLAYER_MODEL_SIZE)
