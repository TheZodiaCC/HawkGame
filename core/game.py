import pygame as pg
import time
from core.consts import WindowConsts, GameConsts
from core.render.window import Window
from game_modules.entities.player import Player
from core.controllers.player_controller import PlayerController


class Game:
    def __init__(self):
        self.window = Window(self, WindowConsts.SCREEN_WIDTH, WindowConsts.SCREEN_HEIGHT, WindowConsts.CAPTION_TEXT)
        self.is_running = False

        self.clock = pg.time.Clock()
        self.delta_time = 0
        self.prev_time = 0

        self.player = Player()
        self.player_controller = PlayerController(self.player)

        self.entities = [self.player]

    def init(self):
        pg.init()
        self.window.init()

        self.is_running = True

    def mainloop(self):
        self.prev_time = time.time()

        while self.is_running:
            self.clock.tick(GameConsts.FPS_LIMIT)

            self.calculate_delta_time()
            self.handle_events(pg.event.get())

            self.player_controller.update(pg.event.get())

            self.window.update()

        self.quit()

    def handle_events(self, events):
        for event in events:
            if event.type == pg.QUIT:
                self.is_running = False

    def calculate_delta_time(self):
        now = time.time()

        self.delta_time = now - self.prev_time
        self.prev_time = now

    def run(self):
        self.init()
        self.mainloop()

    def quit(self):
        pg.quit()
