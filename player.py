import pygame
import math


class Player:
    """the player class"""
    def __init__(self, game):
        self.game = game
        self.worldPos = pygame.Vector2(0, 0)
        self.velocity = pygame.Vector2(0, 0)
        self.speed = 75
        self.radius = 25
        self.rect = pygame.Rect(self.worldPos.x - self.radius, self.worldPos.y - self.radius,
                                self.radius * 2, self.radius * 2)

        # stanima
        self.staminaMax = 100
        self.stamina = self.staminaMax
        self.staminaDrain = 20
        self.staminaRegain = 10
        self.sprintMultiplier = 2.5

    def get_pos(self):
        """getter for the position of the player"""
        return self.worldPos

    def update(self):
        """handles movement and drawing the player to the screen"""
        delta_time = self.game.get_delta_time()
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
            self.velocity.normalize()
            player_speed = self.speed
            if self.stamina > 0 and keys[pygame.K_LSHIFT]:
                player_speed *= self.sprintMultiplier
                self.stamina -= self.staminaDrain * delta_time
                if self.stamina <= 0: self.stamina = 0
            elif self.stamina < 100:
                self.stamina += self.staminaRegain * delta_time
                if self.stamina >= 100: self.stamina = 100
            self.worldPos += self.velocity * player_speed * delta_time
            self.rect = pygame.Rect(self.worldPos.x - self.radius, self.worldPos.y - self.radius,
                                    self.radius * 2, self.radius * 2)

        print(self.stamina)

    def draw(self):
        """draws the player on the screen"""
        screen = self.game.get_screen()
        pygame.draw.circle(screen, "white",
                           (screen.get_width() / 2, screen.get_height() / 2),
                           25)
        pygame.draw.rect(screen, "red", (self.rect.x - self.worldPos.x + screen.get_width() / 2,
                              self.rect.y - self.worldPos.y + screen.get_height() / 2,
                              self.rect.width, self.rect.height))
