import pygame

class LightManager:
    """manages all the lights in the game and handles rendering them to the screen"""
    def __init__(self, game, ambient_color=(0,0,0)):
        """
        initializes the light manager with a reference
        to the game and an ambient color for the light map
        """
        self.game = game
        self.ambient_color = ambient_color
        self.lights = []

        self.light_map = pygame.Surface(self.game.screen.get_size(), pygame.SRCALPHA).convert_alpha()

    def get_lights(self):
        """getter for the list of lights"""
        return self.lights

    def add_light(self, light):
        """adds a light to the list of lights to be rendered"""
        self.lights.append(light)

    def clear(self):
        """clears all the lights from the list"""
        self.lights.clear()

    def render(self, player_pos):
        """
        renders all the lights to the screen by first filling the light map with the ambient color,
        then rendering each light onto the light map, and finally blitting the light map
        onto the screen with a multiply blend mode
        """
        screen = self.game.get_screen()
        self.light_map.fill(self.ambient_color + (255,))

        for light in self.lights:
            light.render(self.light_map, player_pos)

        screen.blit(self.light_map, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
