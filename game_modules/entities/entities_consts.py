import os
from core.core_consts import WorldConsts


class PlayerConsts:
    MODEL_PATH = os.path.join("graphic", "player", "player.png")
    MODEL_SIZE = (50, 50)
    MOVEMENT_SPEED = 4
    FOV = 40
    FOV_RADIUS = WorldConsts.FOV_RADIUS
