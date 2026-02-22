import pygame
import math


class Player:
    """the player class"""
    def __init__(self, game):
        self.game = game
        self.worldPos = pygame.Vector2(0, 0)
        self.velocity = pygame.Vector2(0, 0)
        self.speed = 100

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
            self.worldPos += self.velocity * self.speed * delta_time

    def draw(self):
        """draws the player on the screen"""
        screen = self.game.get_screen()
        pygame.draw.circle(screen, "white",
                           (screen.get_width() / 2, screen.get_height() / 2),
                           25)
