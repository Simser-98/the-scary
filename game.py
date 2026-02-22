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

        self.dark_background = self.make_dark_background()
        self.light_mask = self.make_light_mask(2)

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

    def make_dark_background(self, alpha=255):
        """creates a dark background surface with the specified alpha value"""
        surface = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA).convert_alpha()
        surface.fill((0, 0, 0))
        return surface

    def make_light_mask(self, radius_multiplier, gradient_step=1):
        radius = self.player.get_radius()
        size = radius * radius_multiplier
        mask = pygame.Surface((size, size), pygame.SRCALPHA).convert_alpha()
        position = self.player.get_pos()

        for r in range(radius, 0, -gradient_step):
            alpha = int(255 * (r / radius))
            pygame.draw.circle(mask, (255, 255, 255, alpha), position, r)

        return mask

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
            self.draw_light()
            pygame.display.flip()

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

    def draw_light(self):
        dark = self.dark_background.copy()

        dark.blit(self.light_mask, (self.screen.get_width()/2, self.screen.get_height()/2), special_flags=pygame.BLEND_RGBA_ADD)

        self.screen.blit(dark, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)