class EntityBase:
    def __init__(self):
        self.position = [0, 0]
        self.orientation_target_point = None

        self.fov = 0
        self.fov_radius = 0

        self.render_object = None
        self.collider = None

    def set_orientation_target_point(self, dest_vector):
        self.orientation_target_point = dest_vector
