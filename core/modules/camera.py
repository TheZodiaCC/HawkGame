class Camera:
    def __init__(self):
        self.position = [0, 0]
        self.is_freecam_on = False

    def switch_freecam(self):
        self.is_freecam_on = not self.is_freecam_on
