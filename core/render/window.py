import pygame as pg
from core.core_consts import WindowConsts
from core.utils import screen_utils


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

    def update_frame(self):
        frame = self.frame

        if self.screen_width != WindowConsts.DESIGN_SCREEN_WIDTH and self.screen_height != WindowConsts.DESIGN_SCREEN_HEIGHT:
            frame = pg.transform.scale(frame, (self.screen_width, self.screen_height))

        self.window.blit(frame, frame.get_rect())

    def update(self):
        self.frame.fill((0, 0, 0))

        self.handle_entities()
        self.update_ui()

        self.update_frame()

        pg.display.update()

    def update_ui(self):
        if self.game.is_debug_mode_on:
            self.game.debug_controller.update_debug_data()

            self.game.debug_controller.render_debug_info()

    def handle_entities(self):
        for entity in self.game.objects_manager.game_objects:
            self.render_entity(entity)

            if self.game.is_debug_mode_on:
                self.frame = self.game.debug_controller.draw_entity_debug(entity, self.frame)

    def render_entity(self, entity):
        camera_position = self.game.camera.position

        if screen_utils.check_object_visibility(entity, camera_position):
            transformed_position, rotated_model = entity.render_object.calculate_render_position(camera_position)

            self.frame.blit(rotated_model, transformed_position)
