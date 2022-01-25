import os
from core.consts import WindowConsts


class PlayerConsts:
    PLAYER_MODEL_PATH = os.path.join("graphic", "player", "player.png")
    PLAYER_MODEL_SIZE = (50, 50)
    PLAYER_MODEL_ORIGIN_POINT = (WindowConsts.SCREEN_WIDTH / 2, WindowConsts.SCREEN_HEIGHT / 2)
