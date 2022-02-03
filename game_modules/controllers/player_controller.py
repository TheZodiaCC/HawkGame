import pygame as pg
from game_modules.entities.consts import PlayerConsts
from core.utils import screen_utils
from core.consts import WindowConsts


class PlayerController:
    def __init__(self, game):
        self.game = game

        self.player = self.game.objects_manager.player
        self.player_speed = PlayerConsts.PLAYER_MOVEMENT_SPEED

        self.is_freecam_on = False
        self.move_object = self.player

    def update(self, dt):
        self.handle_rotation()
        self.handle_movement(dt)

    def handle_rotation(self):
        if pg.mouse.get_focused():
            if not self.is_freecam_on:
                converted_dest_vector = screen_utils.convert_point_to_different_resolution(
                    [WindowConsts.SCREEN_WIDTH, WindowConsts.SCREEN_HEIGHT], pg.mouse.get_pos())

                self.player.set_orientation_target_point(converted_dest_vector)

    def switch_freecam(self):
        self.is_freecam_on = not self.is_freecam_on

        if self.is_freecam_on:
            self.move_object = self.game.camera

        else:
            self.move_object = self.player

    def handle_keys(self, key):
        if key == pg.K_f:
            self.switch_freecam()

        elif key == pg.K_g:
            self.game.switch_debug_mode()

    def handle_movement(self, dt):
        key = pg.key.get_pressed()

        if key[pg.K_LEFT]:
            self.move_object.position[0] -= self.player_speed * dt

        if key[pg.K_RIGHT]:
            self.move_object.position[0] += self.player_speed * dt

        if key[pg.K_UP]:
            self.move_object.position[1] -= self.player_speed * dt

        if key[pg.K_DOWN]:
            self.move_object.position[1] += self.player_speed * dt

        self.game.camera.position = self.move_object.position[:]
