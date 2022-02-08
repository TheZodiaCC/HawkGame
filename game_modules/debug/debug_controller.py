import pygame as pg
from core.utils import screen_utils, vectors_utils
from game_modules.debug.debug_consts import DebugConsts
from game_modules.entities.player import Player


class DebugController:
    def __init__(self, game):
        self.game = game

        self.fps_count = None
        self.camera_pos = None
        self.is_debug_on = None
        self.is_freecam_on = None
        self.player_pos = None
        self.player_model_pos = None
        self.player_orientation_pos = None

        self.prev_debug_ui_update = 0

    def update_debug_data(self):
        self.game.debug_controller.prev_debug_ui_update += self.game.clock.tick()

        if self.game.debug_controller.prev_debug_ui_update > 20:
            self.fps_count = int(self.game.clock.get_fps())
            self.camera_pos = self.game.camera.position
            self.is_debug_on = self.game.is_debug_mode_on
            self.is_freecam_on = self.game.camera.is_freecam_on
            self.player_pos = self.game.entities_manager.player.position
            self.player_model_pos = self.game.entities_manager.player.render_object.position
            self.player_orientation_pos = self.game.entities_manager.player.orientation_target_point

    def get_debug_data(self):
        debug_data = [
            f"FPS: {self.fps_count}",
            f"Camera Pos: {self.camera_pos}",
            f"Debug: {self.is_debug_on}",
            f"Freecam: {self.is_freecam_on}",
            f"Player Pos: {self.player_pos}",
            f"Player Model Pos: {self.player_model_pos}",
            f"Player Orientation Point: {self.player_orientation_pos}"
        ]

        return debug_data

    def draw_entity_debug(self, entity, frame):
        pos = entity.render_object.position
        screen_pos = screen_utils.convert_game_position_to_screen_position(entity.position, self.game.camera.position)

        pg.draw.circle(frame, DebugConsts.RENDER_OBJECT_MODEL_POSITION_COLOR, pos, 2, 2)
        pg.draw.circle(frame, DebugConsts.OBJECT_SCREEN_CONVERTED_POSITION_COLOR, screen_pos, 10, 2)

        pg.draw.rect(frame, DebugConsts.RENDER_OBJECT_RECT_COLOR, entity.render_object.rect, 2, 2)

        target_point = entity.orientation_target_point

        if isinstance(entity, Player):
            if target_point and not self.game.camera.is_freecam_on:
                pg.draw.line(frame, DebugConsts.AIM_LINE_COLOR, screen_pos, target_point, 2)

                pg.draw.circle(frame, DebugConsts.RENDER_OBJECT_RECT_COLOR, screen_pos, entity.fov_radius, 2)

                angle_between_target = vectors_utils.get_angle_between_vectors(target_point, screen_pos)

                first_fov_point = vectors_utils.get_point_on_circle(screen_pos, entity.fov_radius, angle_between_target + entity.fov / 2)
                second_fov_point = vectors_utils.get_point_on_circle(screen_pos, entity.fov_radius, angle_between_target - entity.fov / 2)

                pg.draw.line(frame, DebugConsts.AIM_LINE_COLOR, pos, first_fov_point, 2)
                pg.draw.line(frame, DebugConsts.AIM_LINE_COLOR, pos, second_fov_point, 2)

                for ent in self.game.entities_manager.entities:
                    if not isinstance(ent, Player):
                        entitiy_screen_pos = screen_utils.convert_game_position_to_screen_position(
                            ent.position, self.game.camera.position)

                        entity_pos_fov_point = vectors_utils.get_point_on_circle(screen_pos, entity.fov_radius,
                                                                             vectors_utils.get_angle_between_vectors(entitiy_screen_pos, screen_pos))

                        # pg.draw.line(frame, DebugConsts.ENTITIES_LINE, pos, entitiy_screen_pos, 2)
                        pg.draw.line(frame, DebugConsts.ENTITIES_LINE, pos, entity_pos_fov_point, 2)

        return frame

    def render_debug_info(self):
        debug_data = self.get_debug_data()

        next_data_y = 0
        font_size = 30

        for data in debug_data:
            self.game.window.render_text(DebugConsts.TEXT_COLOR, (0, next_data_y), font_size, data)

            next_data_y += font_size
