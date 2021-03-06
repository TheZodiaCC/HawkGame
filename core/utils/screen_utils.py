from core.core_consts import WindowConsts, GameConsts, WorldConsts
from game_modules.entities.entities_consts import PlayerConsts
from core.utils import vectors_utils


def convert_point_to_different_resolution(current_resolution, cords):
    current_width = current_resolution[0]
    current_height = current_resolution[1]

    new_x = linear_conversion(current_width, 0, WindowConsts.DESIGN_SCREEN_WIDTH, 0, cords[0])
    new_y = linear_conversion(current_height, 0, WindowConsts.DESIGN_SCREEN_HEIGHT, 0, cords[1])

    return [new_x, new_y]


def linear_conversion(old_max, old_min, new_max, new_min, old_value):
    old_range = (old_max - old_min)
    new_range = (new_max - new_min)
    new_value = (((old_value - old_min) * new_range) / old_range) + new_min

    return new_value


def check_object_visibility(object, camera_position):
    visible = False

    camera_width = GameConsts.CAMERA_RESOLUTION_WIDTH
    camera_height = GameConsts.CAMERA_RESOLUTION_HEIGHT

    object_x_min = object.position[0]
    object_y_min = object.position[1]
    object_x_max = object.position[0] + object.render_object.model_size[0]
    object_y_max = object.position[1] + object.render_object.model_size[0]

    camera_x_min = camera_position[0] - camera_width / 2
    camera_y_min = camera_position[1] - camera_height / 2
    camera_x_max = camera_position[0] + camera_width / 2
    camera_y_max = camera_position[1] + camera_height / 2

    if camera_x_max >= object_x_min >= camera_x_min and camera_y_max >= object_y_min >= camera_y_min or \
            camera_x_max >= object_x_max >= camera_x_min and camera_y_max >= object_y_max >= camera_y_min:

        visible = True

    return visible


def check_if_in_fov_radius(object_position, camera_position):
    in_fov = False

    distance_between_objects = vectors_utils.get_distance_between_vectors(object_position, camera_position)

    if distance_between_objects <= WorldConsts.FOV_RADIUS / WorldConsts.WORLD_SIZE_TO_PIXELS_FACTOR:
        in_fov = True

    return in_fov


def check_if_in_fov_cone(object_position, camera_position, player_orientation_point):
    visible = False

    fov_radius = WorldConsts.FOV_RADIUS

    object_screen_pos = convert_game_position_to_screen_position(object_position, camera_position)
    player_screen_pos = convert_game_position_to_screen_position(camera_position, camera_position)

    first_fov_point, second_fov_point = get_player_fov_cone_points(player_orientation_point, camera_position)

    entity_pos_fov_point = vectors_utils.get_point_on_circle(player_screen_pos, fov_radius,
                                                             vectors_utils.get_angle_between_vectors(object_screen_pos,
                                                                                                     player_screen_pos))

    if vectors_utils.check_if_vector_between_two_vectors_on_circle(player_screen_pos, first_fov_point,
                                                                   second_fov_point, entity_pos_fov_point):
        visible = True

    return visible


def convert_game_position_to_screen_position(object_position, camera_position):
    camera_width = GameConsts.CAMERA_RESOLUTION_WIDTH
    camera_height = GameConsts.CAMERA_RESOLUTION_HEIGHT

    object_x_pixels_position = object_position[0] * WorldConsts.WORLD_SIZE_TO_PIXELS_FACTOR
    object_y_pixels_position = object_position[1] * WorldConsts.WORLD_SIZE_TO_PIXELS_FACTOR

    converted_position = [object_x_pixels_position, object_y_pixels_position]

    camera_x_min = camera_position[0] * WorldConsts.WORLD_SIZE_TO_PIXELS_FACTOR - camera_width / 2
    camera_y_min = camera_position[1] * WorldConsts.WORLD_SIZE_TO_PIXELS_FACTOR - camera_height / 2
    camera_x_max = camera_position[0] * WorldConsts.WORLD_SIZE_TO_PIXELS_FACTOR + camera_width / 2
    camera_y_max = camera_position[1] * WorldConsts.WORLD_SIZE_TO_PIXELS_FACTOR + camera_height / 2

    converted_position[0] = linear_conversion(camera_x_max, camera_x_min, WindowConsts.DESIGN_SCREEN_WIDTH,
                                              0, converted_position[0])
    converted_position[1] = linear_conversion(camera_y_max, camera_y_min, WindowConsts.DESIGN_SCREEN_HEIGHT,
                                              0, converted_position[1])

    return converted_position


def get_player_fov_cone_points(player_target_point, camera_position):
    fov_radius = WorldConsts.FOV_RADIUS
    player_fov = PlayerConsts.FOV

    player_screen_pos = convert_game_position_to_screen_position(camera_position, camera_position)

    angle_between_target = vectors_utils.get_angle_between_vectors(player_target_point, player_screen_pos)

    first_fov_point = vectors_utils.get_point_on_circle(player_screen_pos, fov_radius,
                                                        angle_between_target + player_fov / 2)
    second_fov_point = vectors_utils.get_point_on_circle(player_screen_pos, fov_radius,
                                                         angle_between_target - player_fov / 2)

    return first_fov_point, second_fov_point

