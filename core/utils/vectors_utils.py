import math


def get_degrees_between_vectors(first_vector, second_vector):
    f_x = first_vector[0]
    f_y = first_vector[1]
    s_x = second_vector[0]
    s_y = second_vector[1]

    radians = math.atan2(-(s_y - f_y), s_x - f_x)
    degrees = math.degrees(radians) - 270

    return degrees
