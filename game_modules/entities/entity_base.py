class EntityBase:
    def __init__(self):
        self.position = [0, 0]
        self.orientation_target_point = None

        self.render_object = None

    def get_position(self):
        return self.position

    def get_orientation_target_point(self):
        return self.orientation_target_point

    def set_orientation_target_point(self, dest_vector):
        self.orientation_target_point = dest_vector
