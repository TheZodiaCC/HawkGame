from game_modules.entities.entity_base import EntityBase
from core.render.render_object import RenderObject
import os


class Player(EntityBase):
    def __init__(self):
        super().__init__()

        self.render_object = RenderObject(os.path.join(os.path.join("graphic", "player"), "player.png"), (50, 50))
        self.rect = None
        self.position = [0, 0]
