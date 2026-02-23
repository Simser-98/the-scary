import pygame, math

from light import Light, calculate_color

def create_cone_surface(radius, player_radius, direction, spread, color, angle_step, radius_step):
    size = radius * 2
    surface = pygame.Surface((size, size), pygame.SRCALPHA).convert_alpha()
    angle_step = max(1, angle_step)
    angle_steps = int(spread / angle_step) + 1

    for r in range(radius, player_radius, -max(1, radius_step)):
        origin_point = pygame.Vector2(radius + player_radius, radius).rotate(direction) # + pygame.Vector2(radius, radius)
        point = pygame.Vector2(r-player_radius, 0).rotate(direction-spread/2)
        cone_points = [origin_point, point + origin_point]
        for a in range(1, angle_steps):
            cone_points.append(point.rotate(a * angle_step) + origin_point)

        draw_color = calculate_color(r, radius, color)
        pygame.draw.polygon(surface, draw_color, cone_points)

    return surface


class ConeLight(Light):
    def __init__(self, game, player_radius, world_pos, radius, spread,
                 direction=0, angle_step=1, **kwargs):
        super().__init__(game, player_radius, world_pos, radius, **kwargs)
        self.spread = spread
        self.direction = direction

        self.rotation_cache = {}
        self.cache_step = 1

        self.surface = create_cone_surface(radius, player_radius, direction, spread,
                                           self.color, angle_step, kwargs["step"] if "step" in kwargs else 1)
        self.bake_angles()

    def bake_angles(self):
        for (angle) in range(0, 360, max(1, self.cache_step)):
            self.rotation_cache[angle] = pygame.transform.rotate(self.surface, -angle)

    def set_direction(self, direction):
        self.direction = direction % 360
        self.surface = self.get_rotated()

    def get_rotated(self):
        key = int(round(self.direction / self.cache_step) * self.cache_step) % 360
        surface = self.rotation_cache.get(key)
        if surface is None:
            surface = pygame.transform.rotate(self.surface, -key)
            self.rotation_cache[key] = surface
        return surface