import pygame


class Player:
    """the player class"""
    def __init__(self, game):
        self.game = game
        self.worldPos = pygame.Vector2(0, 0)

    def get_pos(self):
        """getter for the position of the player"""
        return self.worldPos

    def update(self):
        """handles movement and drawing the player to the screen"""
        delta_time = self.game.get_delta_time()
        keys = self.game.get_keys()
        if keys[pygame.K_w]:
            self.worldPos.y -= 1 * delta_time
        if keys[pygame.K_s]:
            self.worldPos.y += 1 * delta_time
        if keys[pygame.K_a]:
            self.worldPos.x -= 1 * delta_time
        if keys[pygame.K_d]:
            self.worldPos.x += 1 * delta_time

    def draw(self):
        """draws the player on the screen"""
        screen = self.game.get_screen()
        pygame.draw.circle(screen, "white",
                           (screen.get_width() / 2, screen.get_height() / 2),
                           40)
