from core.consts import WindowConsts


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
