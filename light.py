import pygame

def create_radial_surface(radius, player_radius, color, step):
    size = radius * 2
    surface = pygame.Surface((size, size), pygame.SRCALPHA).convert_alpha()

    for r in range(radius, player_radius, -max(1, step)):
        brightness = (-(r / radius) + 1) ** 4
        alpha_value = int(255 * brightness)
        draw_color = (int(color[0] * brightness),
                      int(color[1] * brightness),
                      int(color[2] * brightness),
                      alpha_value)
        pygame.draw.circle(surface, draw_color, (radius, radius), r)

    return surface

class Light:
    def __init__(self, game, player_radius, world_pos, radius, color=(255,255,255), bind_to_player=False, step=1):
        self.game = game
        self.worldPos = world_pos
        self.radius = int(radius)
        self.color = color

        self.bind_to_player = bind_to_player

        self.surface = create_radial_surface(self.radius, player_radius, self.color, step)

    def render(self, light_map, player_pos):
        if self.bind_to_player:
            light_pos = pygame.Vector2((self.game.screen.get_width()-self.surface.get_width())//2,
                                       (self.game.screen.get_height()-self.surface.get_height())//2)
        else:
            light_pos = self.worldPos - player_pos + self.game.screen.getSize() / 2

        light_map.blit(self.surface, light_pos, special_flags=pygame.BLEND_RGBA_ADD)
