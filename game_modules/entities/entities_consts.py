import os
from core.core_consts import WindowConsts, WorldConsts


class PlayerConsts:
    PLAYER_MODEL_PATH = os.path.join("graphic", "player", "player.png")
    PLAYER_MODEL_SIZE = (50, 50)
    PLAYER_MODEL_ORIGIN_POINT = (WindowConsts.DESIGN_SCREEN_WIDTH / 2, WindowConsts.DESIGN_SCREEN_HEIGHT / 2)
    PLAYER_MOVEMENT_SPEED = 4
    PLAYER_FOV = 40
    PLAYER_FOV_RADIUS = WorldConsts.FOV_RADIUS
