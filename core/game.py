import pygame as pg
import time
from core.consts import WindowConsts, GameConsts
from core.objects_manager import ObjectsManager
from core.render.window import Window
from core.modules.camera import Camera
from game_modules.controllers.player_controller import PlayerController
from game_modules.debug.debug_controller import DebugController


class Game:
    def __init__(self):
        self.window = Window(self, WindowConsts.SCREEN_WIDTH, WindowConsts.SCREEN_HEIGHT, WindowConsts.CAPTION_TEXT)
        self.is_running = False

        self.clock = pg.time.Clock()
        self.delta_time = 0

        self.objects_manager = None
        self.camera = Camera()

        self.is_debug_mode_on = False
        self.debug_controller = None

        self.player_controller = None

    def init(self):
        pg.init()

        self.objects_manager = ObjectsManager()
        self.objects_manager.add_debug_object()

        self.objects_manager.init_player()

        self.player_controller = PlayerController(self)

        self.camera.position = self.objects_manager.player.position[:]

        self.window.init()

        self.is_running = True

    def mainloop(self):
        prev_time = time.time()

        while self.is_running:
            self.clock.tick(GameConsts.FPS_LIMIT)

            prev_time = self.calculate_delta_time(prev_time)
            self.handle_events(pg.event.get())

            self.player_controller.update(self.delta_time)

            self.window.update()

        self.quit()

    def handle_events(self, events):
        for event in events:
            if event.type == pg.QUIT:
                self.is_running = False

            elif event.type == pg.KEYUP:
                self.player_controller.handle_keys(event.key)

    def calculate_delta_time(self, prev_time):
        now = time.time()

        self.delta_time = now - prev_time

        return now

    def run(self):
        self.init()
        self.mainloop()

    def quit(self):
        pg.quit()

    def switch_debug_mode(self):
        self.is_debug_mode_on = not self.is_debug_mode_on

        if self.is_debug_mode_on:
            self.debug_controller = DebugController(self)

        else:
            self.debug_controller = None
