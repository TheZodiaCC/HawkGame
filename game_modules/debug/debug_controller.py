class DebugController:
    def __init__(self, game):
        self.game = game

        self.fps_count = None
        self.camera_pos = None
        self.is_debug_on = None
        self.is_freecam_on = None
        self.player_pos = None
        self.player_model_pos = None
        self.player_orientation_pos = None

        self.prev_debug_ui_update = 0

    def update_debug_data(self):
        self.game.debug_controller.prev_debug_ui_update += self.game.clock.tick()

        if self.game.debug_controller.prev_debug_ui_update > 20:
            self.fps_count = int(self.game.clock.get_fps())
            self.camera_pos = self.game.camera.get_position()
            self.is_debug_on = self.game.is_debug_mode_on
            self.is_freecam_on = self.game.player_controller.is_freecam_on
            self.player_pos = self.game.objects_manager.player.get_position()
            self.player_model_pos = self.game.objects_manager.player.render_object.position
            self.player_orientation_pos = self.game.objects_manager.player.get_orientation_target_point()

    def get_debug_data(self):
        debug_data = [
            f"FPS: {self.fps_count}",
            f"Camera Pos: {self.camera_pos}",
            f"Debug: {self.is_debug_on}",
            f"Freecam: {self.is_freecam_on}",
            f"Player Pos: {self.player_pos}",
            f"Player Model Pos: {self.player_model_pos}",
            f"Player Orientation Point: {self.player_orientation_pos}"
        ]

        return debug_data
