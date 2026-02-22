import pygame
from player import Player

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.running = True
        self.delta_time = 0
        self.keys = pygame.key.get_pressed()

        self.player = Player(self)

    def get_screen(self):
        return self.screen

    def get_clock(self):
        return self.clock

    def get_delta_time(self):
        return self.delta_time

    def get_keys(self):
        return self.keys

    def run(self):
        while self.running:
            self.delta_time = self.clock.tick() / 1000
            self.keys = pygame.key.get_pressed()

            self.handle_events()
            self.update()
            self.draw()

        pygame.quit()


    def handle_events(self):
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False


    def update(self):
        self.player.update()

    def draw(self):
        self.screen.fill("black")
        self.player.draw()
        pygame.display.flip()