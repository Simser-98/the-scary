import pygame

def create_radial_surface(radius, color, intensity, steps=60):
    size = radius * 2
    surface = pygame.Surface((size, size), pygame.SRCALPHA).convert_alpha()
    circle_x = circle_y = radius

    for r in range(radius, 0, -max(1, radius//steps)):
        radius_normal = r / radius
        falloff = 1.0 / (1.0 + (radius_normal ** 2))
        brightness = max(0.0, min(1.0, intensity * falloff))
        alpha_value = int(255 * brightness)
        draw_color = (int(color[0] * brightness),
                      int(color[1] * brightness),
                      int(color[2] * brightness),
                      alpha_value)
        pygame.draw.circle(surface, draw_color, (circle_x, circle_y), r)

    return surface

class Light:
    def __init__(self, game, world_pos, radius, color=(255,255,255), intensity=1.0, bind_to_player=False):
        self.game = game
        self.worldPos = world_pos
        self.radius = int(radius)
        self.color = color
        self.intensity = float(intensity)

        self.bind_to_player = bind_to_player

        self.surface = create_radial_surface(self.radius, self.color, self.intensity)

    def render(self, light_map, player_pos):
        if self.bind_to_player:
            light_pos = pygame.Vector2(self.game.screen.get_size()//2)
        else:
            light_pos = self.worldPos - player_pos + self.game.screen.getSize() / 2

        light_map.blit(self.surface, light_pos, special_flags=pygame.BLEND_RGBA_ADD)
