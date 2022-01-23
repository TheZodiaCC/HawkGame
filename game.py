import pygame as pg


class Game:
    def __init__(self):
        self.screen_width = 300
        self.screen_height = 250

        self.window = None
        self.is_running = False

    def init(self):
        self.window = pg.display.set_mode((self.screen_width, self.screen_height))

    def mainloop(self):
        while self.is_running:
            self.handle_events(pg.event.get())

        self.quit()

    def handle_events(self, events):
        for event in events:
            if event.type == pg.QUIT:
                self.is_running = False

    def run(self):
        self.init()

        self.is_running = True

        self.mainloop()

    def quit(self):
        pg.quit()
