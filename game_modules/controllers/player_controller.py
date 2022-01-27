import pygame as pg
from game_modules.entities.consts import PlayerConsts


class PlayerController:
    def __init__(self, player):
        self.player = player

        self.player_speed = PlayerConsts.PLAYER_MOVEMENT_SPEED

    def update(self, dt):
        self.handle_rotation()
        self.handle_movement(dt)

    def handle_rotation(self):
        if pg.mouse.get_focused():
            self.player.set_orientation_target_point(pg.mouse.get_pos())

    def handle_movement(self, dt):
        key = pg.key.get_pressed()

        if key[pg.K_LEFT]:
            self.player.position[0] -= self.player_speed * dt

        if key[pg.K_RIGHT]:
            self.player.position[0] += self.player_speed * dt

        if key[pg.K_UP]:
            self.player.position[1] -= self.player_speed * dt

        if key[pg.K_DOWN]:
            self.player.position[1] += self.player_speed * dt
