import math

import pygame


def clamp(value, min_value, max_value):
    """clamps a value between a minimum and maximum value"""
    return max(min_value, min(value, max_value))

def circle_rect_collides(circle_pos, radius, rectangle):
    """checks for collision between a circle and a rectangle"""
    closest_x = clamp(circle_pos.x, rectangle.left, rectangle.right)
    closest_y = clamp(circle_pos.y, rectangle.top, rectangle.bottom)

    distance_x = circle_pos.x - closest_x
    distance_y = circle_pos.y - closest_y

    distance_squared = distance_x ** 2 + distance_y ** 2
    return distance_squared < radius ** 2


class Player:
    """the player class"""
    def __init__(self, game):
        self.game = game
        self.worldPos = pygame.Vector2(100, 100)
        self.velocity = pygame.Vector2(0, 0)
        self.speed = 75
        self.radius = 25

        # stanima
        self.staminaMax = 100
        self.stamina = self.staminaMax
        self.staminaDrain = 20
        self.staminaRegain = 10
        self.sprintMultiplier = 2.5

    def get_pos(self):
        """getter for the position of the player"""
        return self.worldPos

    def handle_collisions(self, colliders, player_speed, delta_time):
        """handles collisions with the walls and props in the world"""
        displacement = self.velocity * player_speed * delta_time

        temp_pos = self.worldPos + displacement

        search_rect = pygame.Rect(
            temp_pos.x - self.radius * 2 + displacement.x,
            temp_pos.y - self.radius * 2 + displacement.y,
            self.radius * 4,
            self.radius * 4
        )

        for collider in colliders:
            if not collider.colliderect(search_rect):
                continue

            if circle_rect_collides(temp_pos, self.radius, collider):
                closest_x = clamp(temp_pos.x, collider.left, collider.right)
                closest_y = clamp(temp_pos.y, collider.top, collider.bottom)

                distance_x = closest_x - temp_pos.x
                distance_y = closest_y - temp_pos.y
                resolve_on_y = abs(distance_x) < abs(distance_y)
                if resolve_on_y:
                    primary_distance = distance_y
                    secondary_distance = distance_x
                    primary_displacement = displacement.y
                else:
                    primary_distance = distance_x
                    secondary_distance = distance_y
                    primary_displacement = displacement.x
                if primary_displacement != 0:
                    if resolve_on_y:
                        temp_pos.y = self.worldPos.y
                    else:
                        temp_pos.x = self.worldPos.x
                else:
                    overlap = math.sqrt(self.radius ** 2 - secondary_distance ** 2) - abs(primary_distance)
                    correction = overlap * (1 if primary_distance > 0 else -1)

                    if resolve_on_y:
                        temp_pos.y -= correction
                    else:
                        temp_pos.x -= correction

        self.worldPos = temp_pos

    def update(self, colliders):
        """handles movement and drawing the player to the screen"""
        delta_time = self.game.get_delta_time()
        print(self.stamina)
        keys = self.game.get_keys()
        self.velocity = pygame.Vector2(0, 0)
        if keys[pygame.K_w]:
            self.velocity.y -= 1
        if keys[pygame.K_s]:
            self.velocity.y += 1
        if keys[pygame.K_a]:
            self.velocity.x -= 1
        if keys[pygame.K_d]:
            self.velocity.x += 1

        if self.velocity.length() != 0:
            self.velocity = self.velocity.normalize()
            player_speed = self.speed
            if self.stamina > 0 and keys[pygame.K_LSHIFT]:
                player_speed *= self.sprintMultiplier
                self.stamina -= self.staminaDrain * delta_time
                if self.stamina <= 0: self.stamina = 0
            elif self.stamina < 100:
                self.stamina += self.staminaRegain * delta_time
                if self.stamina >= 100: self.stamina = 100

            self.handle_collisions(colliders, player_speed, delta_time)

        elif self.stamina < 100:
            self.stamina += self.staminaRegain * delta_time
            if self.stamina >= 100: self.stamina = 100

    def draw(self):
        """draws the player on the screen"""
        screen = self.game.get_screen()
        pygame.draw.circle(screen, "white",
                           (screen.get_width() / 2, screen.get_height() / 2),
                           25)
