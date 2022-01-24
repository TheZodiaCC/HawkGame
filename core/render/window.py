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
        self.window = pg.display.set_mode((self.screen_width, self.screen_height))
        pg.display.set_caption(self.screen_caption_text)

    def render_text(self, color, position, size, text):
        font = pg.font.SysFont(WindowConsts.DEFAULT_FONT, size)
        text = font.render(text, False, color)

        self.window.blit(text, position)

    def render_pointer(self):
        x, y = pg.mouse.get_pos()

        pg.draw.circle(self.window, (255, 255, 255), (x, y), 10, 1)

    def update(self):
        self.window.fill((0, 0, 0))

        self.update_ui()
        self.handle_entities()
        # self.render_pointer()

        pg.display.update()

    def update_ui(self):
        self.render_debug_info()

    def handle_entities(self):
        for entity in self.game.entities:
            self.render_entity(entity)

    def render_entity(self, entity):
        model = pg.transform.rotate(entity.model, entity.orientation_diff)

        pos = [entity.get_position()[0] - model.get_width() / 2, entity.get_position()[1] - model.get_height() / 2]

        self.window.blit(model, pos)

        # Debug
        pos = entity.get_position()

        pg.draw.circle(self.window, (255, 0, 0), pos, 2, 2)
        pg.draw.circle(self.window, (255, 0, 0), pos, 10, 2)

    def render_debug_info(self):
        self.render_text((255, 255, 255), (0, 0), 30, f"FPS: {int(self.game.clock.get_fps())}")
