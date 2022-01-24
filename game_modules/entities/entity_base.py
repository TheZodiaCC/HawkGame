from core.utils import vectors_utils


class EntityBase:
    def __init__(self):
        self.model = None
        self.rect = None
        self.position = [0, 0]

        self.init_entity_model()

        self.orientation_diff = 0

    def init_entity_model(self):
        pass

    def get_position(self):
        return self.position

    def set_orientation(self, dest_vector):
        self.orientation_diff = vectors_utils.get_degrees_between_vectors(dest_vector, self.get_position())
