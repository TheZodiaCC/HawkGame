from core.utils import vectors_utils


class EntityBase:
    def __init__(self):
        self.render_object = None
        self.position = [0, 0]

        self.orientation_diff = 0

    def get_position(self):
        return self.position

    def set_orientation(self, dest_vector):
        self.orientation_diff = vectors_utils.get_degrees_between_vectors(dest_vector, self.get_position())
