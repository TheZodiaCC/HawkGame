import pygame as pg
from core.utils import screen_utils, vectors_utils
from core.core_consts import WorldConsts
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

    def draw_entity_collider(self, entity, frame):
        screen_pos = screen_utils.convert_game_position_to_screen_position(entity.position, self.game.camera.position)

        pg.draw.circle(frame, DebugConsts.OBJECT_SCREEN_CONVERTED_POSITION_COLOR, screen_pos, 10, 2)

        collider_cords = entity.collider.get_world_xywh()

        collider_rect_pos_xy = screen_utils.convert_game_position_to_screen_position(
            [collider_cords[0], collider_cords[1]],
            self.game.camera.position)

        collider_screen_rect = pg.Rect(collider_rect_pos_xy[0], collider_rect_pos_xy[1],
                                       collider_cords[2] * WorldConsts.WORLD_SIZE_TO_PIXELS_FACTOR,
                                       collider_cords[3] * WorldConsts.WORLD_SIZE_TO_PIXELS_FACTOR)

        pg.draw.rect(frame, DebugConsts.COLLIDER_RECT_COLOR, collider_screen_rect, 2, 2)

    def draw_player_debug(self, entity, frame):
        screen_pos = screen_utils.convert_game_position_to_screen_position(entity.position, self.game.camera.position)
        target_point = entity.orientation_target_point

        if target_point and not self.game.camera.is_freecam_on:
            pg.draw.line(frame, DebugConsts.AIM_LINE_COLOR, screen_pos, target_point, 2)

            pg.draw.circle(frame, DebugConsts.RENDER_OBJECT_RECT_COLOR, screen_pos, entity.fov_radius, 2)

            angle_between_target = vectors_utils.get_angle_between_vectors(target_point, screen_pos)

            first_fov_point = vectors_utils.get_point_on_circle(screen_pos, entity.fov_radius,
                                                                angle_between_target + entity.fov / 2)
            second_fov_point = vectors_utils.get_point_on_circle(screen_pos, entity.fov_radius,
                                                                 angle_between_target - entity.fov / 2)

            pg.draw.line(frame, DebugConsts.AIM_LINE_COLOR, screen_pos, first_fov_point, 2)
            pg.draw.line(frame, DebugConsts.AIM_LINE_COLOR, screen_pos, second_fov_point, 2)

            for ent in self.game.entities_manager.entities:
                if not isinstance(ent, Player):
                    entitiy_screen_pos = screen_utils.convert_game_position_to_screen_position(
                        ent.position, self.game.camera.position)

                    entity_pos_fov_point = vectors_utils.get_point_on_circle(screen_pos, entity.fov_radius,
                                                                             vectors_utils.get_angle_between_vectors(
                                                                                 entitiy_screen_pos, screen_pos))

                    entity_line_color = DebugConsts.INVISIBLE_ENTITIES_LINE

                    if vectors_utils.check_if_vector_between_two_vectors_on_circle(screen_pos, first_fov_point,
                                                                                   second_fov_point,
                                                                                   entity_pos_fov_point):
                        entity_line_color = DebugConsts.VISIBLE_ENTITIES_LINE

                    pg.draw.line(frame, entity_line_color, screen_pos, entity_pos_fov_point, 2)

    def draw_entity_debug(self, entity, frame):
        self.draw_entity_collider(entity, frame)

        if isinstance(entity, Player):
            self.draw_player_debug(entity, frame)

        return frame

    def render_debug_info(self):
        debug_data = self.get_debug_data()

        next_data_y = 0
        font_size = 30

        for data in debug_data:
            self.game.window.render_text(DebugConsts.TEXT_COLOR, (0, next_data_y), font_size, data)

            next_data_y += font_size
