import pygame
import csv
from prop import Prop


class World:
    def __init__(self, game, floor):
        self.game = game
        self.walls = []
        self.props = []
        self.floor = floor

    def get_collisions(self):
        """returns a list of all the walls and props in the world for collision detection"""
        return self.walls + [pygame.Rect(prop.get_pos().x, prop.get_pos().y,
                                        prop.get_dimensions().x, prop.get_dimensions().y) for prop in self.props]

    def setup(self):
        """sets up the world with walls and props"""
        with open(self.floor, "r") as f:

            csv_reader = csv.reader(f)
            # skips header row
            next(csv_reader, None)

            for row in csv_reader:
                if "wall" in row[0]:
                    self.walls.append(pygame.Rect(float(row[1]), float(row[2]), float(row[3]), float(row[4])))
                else:
                    self.props.append(Prop(pygame.Vector2(float(row[1]), float(row[2])),pygame.Vector2(float(row[3]), float(row[4]))))
                print(row)

    def draw(self, player_pos):
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