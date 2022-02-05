import math


def get_normalized_rotation_degrees_between_vectors(first_vector, second_vector):
    f_x = first_vector[0]
    f_y = first_vector[1]
    s_x = second_vector[0]
    s_y = second_vector[1]

    radians = math.atan2(-(s_y - f_y), s_x - f_x)
    degrees = math.degrees(radians) - 270

    return degrees


def get_angle_between_vectors(first_vector, second_vector):
    degrees = math.atan2(first_vector[1] - second_vector[1], first_vector[0] - second_vector[0])

    return degrees


def get_point_on_circle(circle_center, circle_radius, offset_angle):
    x = circle_center[0] + (circle_radius * math.cos(offset_angle))
    y = circle_center[1] + (circle_radius * math.sin(offset_angle))

    return [x, y]
