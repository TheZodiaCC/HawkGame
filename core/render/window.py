import pygame as pg
from core.consts import WindowConsts
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
        frame = pg.transform.scale(self.frame, (self.screen_width, self.screen_height))
        self.window.blit(frame, frame.get_rect())

    def update(self):
        self.frame.fill((0, 0, 0))

        self.handle_entities()
        self.update_ui()

        self.update_frame()

        pg.display.update()

    def update_ui(self):
        if self.game.is_debug_mode_on:
            self.render_debug_info()

    def handle_entities(self):
        for entity in self.game.objects_manager.game_objects:
            self.render_entity(entity)

    def render_entity(self, entity):
        camera_position = self.game.camera.get_position()

        if screen_utils.check_object_visibility(entity, camera_position):
            transformed_position, rotated_model = entity.render_object.calculate_render_position(camera_position)

            self.frame.blit(rotated_model, transformed_position)

            if self.game.is_debug_mode_on:
                self.draw_entity_debug(entity)

    def draw_entity_debug(self, entity):
        pos = entity.render_object.position
        screen_pos = screen_utils.convert_game_position_to_screen_position(entity.position, self.game.camera.get_position())

        pg.draw.circle(self.frame, (255, 0, 0), pos, 2, 2)
        pg.draw.circle(self.frame, (255, 0, 0), pos, 10, 2)
        pg.draw.circle(self.frame, (0, 255, 0), [screen_pos[0], screen_pos[1]], 10, 2)

        pg.draw.rect(self.frame, (255, 255, 0), entity.render_object.rect, 2, 2)

        target_point = entity.orientation_target_point

        if target_point:
            tp = screen_utils.convert_point_to_different_resolution(
                [WindowConsts.SCREEN_WIDTH, WindowConsts.SCREEN_HEIGHT], target_point)

            pg.draw.line(self.frame, (255, 255, 255), pos, tp, 2)

    def render_debug_info(self):
        debug_data = [
            f"FPS: {int(self.game.clock.get_fps())}",
            f"Camera Pos: {self.game.camera.get_position()}",
            f"Debug: {self.game.is_debug_mode_on}",
            f"Freecam: {self.game.player_controller.is_freecam_on}",
            f"Player Pos: {self.game.objects_manager.player.get_position()}",
            f"Player Model Pos: {self.game.objects_manager.player.render_object.position}",
            f"Player Orientation Point: {self.game.objects_manager.player.get_orientation_target_point()}"
        ]

        next_data_y = 0
        font_size = 30

        for data in debug_data:
            self.render_text((255, 255, 255), (0, next_data_y), font_size, data)

            next_data_y += font_size
