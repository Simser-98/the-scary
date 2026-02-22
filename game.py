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
        self.floor1 = World(self, "floors/floor_1.csv")
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
        fps_measurements = []
        while self.running:
            self.deltaTime = self.clock.tick() / 1000
            self.keys = pygame.key.get_pressed()

            fps_measurements.append(self.clock.get_fps())
            if len(fps_measurements) > 1000:
                fps_measurements.remove(fps_measurements[0])
            fps_sum = 0
            for i in fps_measurements:
                fps_sum += i
            pygame.display.set_caption("fps: " + str(fps_sum / len(fps_measurements)))

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
        self.player.update(self.floor1.get_colliders())

    def draw(self):
        """draws the game to the screen"""
        self.screen.fill("black")
        self.floor1.draw(self.player.get_pos())
        self.player.draw()
        pygame.display.flip()