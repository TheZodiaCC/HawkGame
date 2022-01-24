import pygame as pg
from core.consts import WindowConsts
from core.utils import screen_utils, vectors_utils


class Window:
    def __init__(self, game, screen_width, screen_height, screen_caption_text):
        self.game = game

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.screen_caption_text = screen_caption_text

        self.window = None
        self.frame = None

    def init(self):
        self.window = pg.display.set_mode((self.screen_width, self.screen_height))
        pg.display.set_caption(self.screen_caption_text)
        self.frame = pg.Surface((WindowConsts.DESIGN_SCREEN_WIDTH, WindowConsts.DESIGN_SCREEN_HEIGHT))

    def render_text(self, color, position, size, text):
        font = pg.font.SysFont(WindowConsts.DEFAULT_FONT, size)
        text = font.render(text, False, color)

        self.frame.blit(text, position)

    def update(self):
        self.frame.fill((0, 0, 0))

        self.update_ui()
        self.handle_entities()

        frame = pg.transform.scale(self.frame, (self.screen_width, self.screen_height))
        self.window.blit(frame, frame.get_rect())

        pg.display.update()

    def update_ui(self):
        self.render_debug_info()

    def handle_entities(self):
        for entity in self.game.entities:
            self.render_entity(entity)

    def handle_entity_rotation(self, entity):
        converted_target_point_cords = screen_utils.convert_point_to_different_resolution(
            [WindowConsts.SCREEN_WIDTH, WindowConsts.SCREEN_HEIGHT], entity.get_orientation_target_point())

        orientation_diff = vectors_utils.get_degrees_between_vectors(converted_target_point_cords, entity.get_position())

        rotated_model = pg.transform.rotate(entity.render_object.model, orientation_diff)

        return rotated_model

    def render_entity(self, entity):
        rotated_model = self.handle_entity_rotation(entity)

        pos = [entity.get_position()[0] - rotated_model.get_width() / 2,
               entity.get_position()[1] - rotated_model.get_height() / 2]

        self.frame.blit(rotated_model, pos)

        self.draw_entity_debug(entity)

    def draw_entity_debug(self, entity):
        pos = entity.get_position()

        pg.draw.circle(self.frame, (255, 0, 0), pos, 2, 2)
        pg.draw.circle(self.frame, (255, 0, 0), pos, 10, 2)

    def render_debug_info(self):
        self.render_text((255, 255, 255), (0, 0), 30, f"FPS: {int(self.game.clock.get_fps())}")
