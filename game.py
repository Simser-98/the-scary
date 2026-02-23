import pygame

from player import Player
from world import World
from lightManager import LightManager
from light import Light
from coneLight import ConeLight


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

        self.light_manager = LightManager(self, ambient_color=(0,0,0))
        self.light_manager.add_light(Light(self, self.player.get_radius(), self.player.get_pos(),
                                           200, color=(127, 127, 127), bind_to_player=True))
        self.light_manager.add_light(ConeLight(self, self.player.get_radius(), self.player.get_pos(),
                                               400, color=(200, 200, 200), bind_to_player=True))

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
        self.screen.fill((96, 59, 42))
        self.floor1.draw(self.player.get_pos())
        self.player.draw()

        # radius = 400
        # player_radius = 25
        # direction = 0
        # angle_steps = 6
        # angle_step = 5
        # draw_color = (255, 255, 255, 255)

        # origin_point = pygame.Vector2(radius, 0).rotate(direction) + pygame.Vector2(25, self.screen.get_height()/2)
        # point = pygame.Vector2(400 - player_radius, 0).rotate(direction)
        # cone_points = [origin_point, point + origin_point]
        # for a in range(1, angle_steps):
        #     cone_points.append(point.rotate(a * angle_step) + origin_point)
        # pygame.draw.polygon(self.screen, draw_color, cone_points)

        self.light_manager.render(self.player.get_pos())

        pygame.display.flip()