import pygame as pg
from game_modules.entities.consts import PlayerConsts


class PlayerController:
    def __init__(self, game):
        self.game = game

        self.player = self.game.objects_manager.player
        self.player_speed = PlayerConsts.PLAYER_MOVEMENT_SPEED

    def update(self, dt):
        self.handle_rotation()
        self.handle_movement(dt)

    def handle_rotation(self):
        if pg.mouse.get_focused():
            self.player.set_orientation_target_point(pg.mouse.get_pos())

    def handle_movement(self, dt):
        key = pg.key.get_pressed()

        move_entity = self.player

        if key[pg.K_LEFT]:
            move_entity.position[0] -= self.player_speed * dt

        if key[pg.K_RIGHT]:
            move_entity.position[0] += self.player_speed * dt

        if key[pg.K_UP]:
            move_entity.position[1] -= self.player_speed * dt

        if key[pg.K_DOWN]:
            move_entity.position[1] += self.player_speed * dt

        self.game.camera.position = move_entity.position
