import pygame as pg
from core.utils import path_utils, screen_utils, vectors_utils


class RenderObject:
    def __init__(self, entity, model_path, model_size):
        self.entity = entity

        self.position = [0, 0]
        self.model = None
        self.rect = None

        self.model_path = model_path
        self.model_size = model_size

        self.init_model()

    def init_model(self):
        self.model = pg.image.load(path_utils.get_abs_path(self.model_path))
        self.model = pg.transform.scale(self.model, self.model_size)

        self.rect = self.model.get_rect()

        self.position = [self.position[0], self.position[1]]

        self.rect.center = self.position

    def handle_entity_rotation(self):
        rotated_model = self.model

        if self.entity.orientation_target_point:
            orientation_diff = vectors_utils.get_normalized_rotation_degrees_between_vectors(self.entity.orientation_target_point,
                                                                         self.entity.render_object.position)

            rotated_model = pg.transform.rotate(self.entity.render_object.model, orientation_diff)

        return rotated_model

    def calculate_render_position(self, camera_position):
        rotated_model = self.handle_entity_rotation()

        screen_position = screen_utils.convert_game_position_to_screen_position(self.entity.position,
                                                                                     camera_position)

        transformed_position = [screen_position[0] - rotated_model.get_width() / 2,
                                screen_position[1] - rotated_model.get_height() / 2]

        self.position = [transformed_position[0] + rotated_model.get_width() / 2,
                         transformed_position[1] + rotated_model.get_width() / 2]

        self.rect.center = self.position

        return transformed_position, rotated_model
