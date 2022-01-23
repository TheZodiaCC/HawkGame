import pygame as pg
from core.consts import WindowConsts
from core.render.window import Window


class Game:
    def __init__(self):
        self.window = Window(WindowConsts.SCREEN_WIDTH, WindowConsts.SCREEN_HEIGHT, WindowConsts.CAPTION_TEXT)
        self.is_running = False

    def init(self):
        self.is_running = True
        self.window.init()

    def mainloop(self):
        while self.is_running:
            self.handle_events(pg.event.get())

            self.window.update()

        self.quit()

    def handle_events(self, events):
        for event in events:
            if event.type == pg.QUIT:
                self.is_running = False

    def run(self):
        self.init()

        self.mainloop()

    def quit(self):
        pg.quit()
