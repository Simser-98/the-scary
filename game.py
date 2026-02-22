import pygame

from player import Player
from world import World


class Game:
    """the main game class"""
    def __init__(self):
        """initializes pygame and sets up the game window and clock"""
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.running = True
        self.deltaTime = 0
        self.keys = pygame.key.get_pressed()

        self.player = Player(self)
        self.floor1 = World(self)
        self.floor1.setup()

    def get_screen(self):
        """getter for the screen surface"""
        return self.screen

    def get_clock(self):
        """getter for the clock object"""
        return self.clock

    def get_delta_time(self):
        """getter for the delta time since the last frame"""
        return self.deltaTime

    def get_keys(self):
        """getter for the current state of the keyboard"""
        return self.keys

    def run(self):
        """the main game loop"""
        while self.running:
            self.deltaTime = self.clock.tick() / 1000
            self.keys = pygame.key.get_pressed()

            self.handle_events()
            self.update()
            self.draw()

        pygame.quit()


    def handle_events(self):
        """handles user input and other events"""
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False


    def update(self):
        """updates the game state"""
        self.player.update()

    def draw(self):
        """draws the game to the screen"""
        self.screen.fill("black")
        self.floor1.draw(self.player.get_pos())
        self.player.draw()
        pygame.display.flip()