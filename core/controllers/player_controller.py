import pygame as pg


class PlayerController:
    def __init__(self, player):
        self.player = player

    def update(self, events):
        self.handle_rotation()

    def handle_rotation(self):
        if pg.mouse.get_focused():
            mouse_x, mouse_y = pg.mouse.get_pos()

            self.player.set_orientation((mouse_x, mouse_y))

    def handle_movement(self):
        pass
