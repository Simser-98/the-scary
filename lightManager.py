import pygame

class LightManager:
    def __init__(self, game, ambient_color=(0,0,0)):
        self.game = game
        self.ambient_color = ambient_color
        self.lights = []

        self.light_map = pygame.Surface(self.game.screen.get_size(), pygame.SRCALPHA).convert_alpha()

    def add_light(self, light):
        self.lights.append(light)

    def clear(self):
        self.lights.clear()

    def render(self, player_pos):
        screen = self.game.get_screen()
        self.light_map.fill(self.ambient_color + (255,))

        for light in self.lights:
            light.render(self.light_map, player_pos)

        screen.blit(self.light_map, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
