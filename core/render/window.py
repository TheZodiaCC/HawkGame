import pygame as pg
from core.consts import WindowConsts


class Window:
    def __init__(self, game, screen_width, screen_height, screen_caption_text):
        self.game = game

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.screen_caption_text = screen_caption_text

        self.window = None

    def init(self):
        self.window = pg.display.set_mode((self.screen_width, self.screen_height), pg.RESIZABLE)
        pg.display.set_caption(self.screen_caption_text)

    def render_text(self, color, position, size, text):
        font = pg.font.SysFont(WindowConsts.DEFAULT_FONT, size)
        text = font.render(text, False, color)

        self.window.blit(text, position)

    def update(self):
        self.window.fill((0, 0, 0))

        self.render_debug_info()

        pg.display.update()

    def render_debug_info(self):
        self.render_text((255, 255, 255), (0, 0), 30, f"FPS: {int(self.game.clock.get_fps())}")
