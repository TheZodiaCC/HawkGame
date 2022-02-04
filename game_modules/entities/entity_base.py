class EntityBase:
    def __init__(self):
        self.position = [0, 0]
        self.orientation_target_point = None

        self.render_object = None

    def set_orientation_target_point(self, dest_vector):
        self.orientation_target_point = dest_vector
