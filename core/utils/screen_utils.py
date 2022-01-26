from core.consts import WindowConsts, GameConsts, WorldConsts


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


def check_object_visibility(object_position, camera_position):
    visible = False

    camera_width = GameConsts.CAMERA_RESOLUTION_WIDTH
    camera_height = GameConsts.CAMERA_RESOLUTION_HEIGHT

    object_x = object_position[0]
    object_y = object_position[1]

    camera_x_min = camera_position[0] - camera_width / 2
    camera_y_min = camera_position[1] - camera_height / 2
    camera_x_max = camera_position[0] + camera_width / 2
    camera_y_max = camera_position[1] + camera_height / 2

    if camera_x_max >= object_x >= camera_x_min and camera_y_max >= object_y >= camera_y_min:
        visible = True

    return visible


def convert_game_position_to_screen_position(object_position, camera_position):
    camera_width = GameConsts.CAMERA_RESOLUTION_WIDTH
    camera_height = GameConsts.CAMERA_RESOLUTION_HEIGHT

    object_x = object_position[0]
    object_y = object_position[1]

    converted_position = [object_x, object_y]

    camera_x_min = camera_position[0] - camera_width / 2
    camera_y_min = camera_position[1] - camera_height / 2
    camera_x_max = camera_position[0] + camera_width / 2
    camera_y_max = camera_position[1] + camera_height / 2

    converted_position[0] = linear_conversion(camera_x_max, camera_x_min, WindowConsts.DESIGN_SCREEN_WIDTH,
                                              0, converted_position[0])
    converted_position[1] = linear_conversion(camera_y_max, camera_y_min, WindowConsts.DESIGN_SCREEN_HEIGHT,
                                              0, converted_position[1])

    return converted_position

