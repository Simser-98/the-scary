import pygame

from prop import Prop


class World:
    def __init__(self, game):
        self.game = game
        self.walls = []
        self.props = []

    def get_colliders(self):
        """returns a list of all the walls and props in the world for collision detection"""
        return self.walls + [pygame.Rect(prop.get_pos().x, prop.get_pos().y,
                                        prop.get_dimensions().x, prop.get_dimensions().y) for prop in self.props]

    def setup(self):
        """sets up the world with walls and props"""
        self.walls.append(pygame.Rect(0, 0, 800, 20))
        self.walls.append(pygame.Rect(0, 580, 800, 20))
        self.walls.append(pygame.Rect(0, 0, 20, 600))
        self.walls.append(pygame.Rect(780, 0, 20, 600))

        self.props.append(Prop(pygame.Vector2(200, 200), pygame.Vector2(50, 50)))
        self.props.append(Prop(pygame.Vector2(400, 300), pygame.Vector2(100, 100)))
        self.props.append(Prop(pygame.Vector2(600, 400), pygame.Vector2(75, 75)))

    def draw(self, player_pos):
        """draws the walls and props to the screen relative to the player's position"""
        screen = self.game.get_screen()
        for wall in self.walls:
            pygame.draw.rect(screen, "white",
                             (wall.x - player_pos.x + screen.get_width() / 2,
                              wall.y - player_pos.y + screen.get_height() / 2,
                              wall.width, wall.height))

        for prop in self.props:
            pygame.draw.rect(screen, "white",
                             (prop.get_pos().x - player_pos.x + screen.get_width() / 2,
                              prop.get_pos().y - player_pos.y + screen.get_height() / 2,
                              prop.get_dimensions().x, prop.get_dimensions().y))