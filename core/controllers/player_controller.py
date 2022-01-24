import pygame as pg
from core.utils import screen_utils
from core.consts import WindowConsts


class PlayerController:
    def __init__(self, player):
        self.player = player

    def update(self, dt):
        self.handle_rotation()
        self.handle_movement(dt)

    def handle_rotation(self):
        if pg.mouse.get_focused():
            mouse_x, mouse_y = pg.mouse.get_pos()

            converted_mouse_cords = screen_utils.convert_point_to_different_resolution(
                [WindowConsts.SCREEN_WIDTH, WindowConsts.SCREEN_HEIGHT], [mouse_x, mouse_y])

            self.player.set_orientation(converted_mouse_cords)

    def handle_movement(self, dt):
        key = pg.key.get_pressed()

        if key[pg.K_LEFT]:
            self.player.position[0] -= 200 * dt

        if key[pg.K_RIGHT]:
            self.player.position[0] += 200 * dt

        if key[pg.K_UP]:
            self.player.position[1] -= 200 * dt

        if key[pg.K_DOWN]:
            self.player.position[1] += 200 * dt
