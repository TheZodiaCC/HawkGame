import pygame as pg


class Window:
    def __init__(self, screen_width, screen_height, screen_caption_text):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.screen_caption_text = screen_caption_text

        self.window = None

    def init(self):
        self.window = pg.display.set_mode((self.screen_width, self.screen_height))
        pg.display.set_caption(self.screen_caption_text)

    def update(self):
        pg.display.update()
