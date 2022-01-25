from game_modules.entities.entity_base import EntityBase
from core.render.render_object import RenderObject
from core.consts import WindowConsts
import os


class Player(EntityBase):
    def __init__(self):
        super().__init__()

        self.render_object = RenderObject(
                                os.path.join(os.path.join("graphic", "player"), "player.png"),
                                (50, 50),
                                True,
                                (WindowConsts.SCREEN_WIDTH / 2, WindowConsts.SCREEN_HEIGHT / 2))
        self.position = [0, 0]
