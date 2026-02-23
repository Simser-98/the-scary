import pygame

def create_radial_surface(radius, player_radius, color, step):
    """creates a radial gradient surface for a light with the specified radius and color"""
    size = radius * 2
    surface = pygame.Surface((size, size), pygame.SRCALPHA).convert_alpha()

    for r in range(radius, player_radius, -max(1, step)):
        draw_color = calculate_color(r, radius, color)
        pygame.draw.circle(surface, draw_color, (radius, radius), r)

    return surface

def calculate_color(r, radius, color):
    """calculates the color and alpha value for a given distance from the center of the light"""
    brightness = (-(r / radius) + 1) ** 5
    alpha_value = int(255 * brightness)
    draw_color = (int(color[0] * brightness),
                  int(color[1] * brightness),
                  int(color[2] * brightness),
                  alpha_value)

    return draw_color

class Light:
    """a simple light that emits in a circular shape, with a radial gradient"""
    def __init__(self, game, player_radius, world_pos, radius, color=(255,255,255), bind_to_player=False, step=1):
        """
        initializes the light with the specified parameters
        and pre-renders the radial gradient surface for faster rendering
        """
        self.game = game
        self.worldPos = world_pos
        self.radius = int(radius)
        self.color = color

        self.bind_to_player = bind_to_player

        self.surface = create_radial_surface(self.radius, player_radius, self.color, step)

    def render(self, light_map, player_pos):
        """
        renders the light onto the light map at the correct position
        based on whether it is bound to the player or not
        """
        if self.bind_to_player:
            light_pos = pygame.Vector2((self.game.screen.get_width()-self.surface.get_width())//2,
                                       (self.game.screen.get_height()-self.surface.get_height())//2)
        else:
            light_pos = self.worldPos - player_pos + self.game.screen.getSize() / 2

        light_map.blit(self.surface, light_pos, special_flags=pygame.BLEND_RGBA_ADD)
