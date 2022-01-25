import pygame as pg


class PlayerController:
    def __init__(self, player):
        self.player = player

    def update(self, dt):
        self.handle_rotation()
        self.handle_movement(dt)

    def handle_rotation(self):
        if pg.mouse.get_focused():
            self.player.set_orientation_target_point(pg.mouse.get_pos())

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

        self.player.render_object.position = self.player.position
