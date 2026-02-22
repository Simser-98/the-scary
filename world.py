import pygame
import csv

import prop
from prop import Prop
from item import Item


class World:
    def __init__(self, game, floor):
        self.game = game
        self.walls = []
        self.props = []
        self.items = []
        self.floor = floor

    def get_colliders(self):
        """returns a list of all the walls and props in the world for collision detection"""
        return self.walls + [pygame.Rect(prop.get_pos().x, prop.get_pos().y,
                                        prop.get_dimensions().x, prop.get_dimensions().y) for prop in self.props]

    def get_items(self):
        """returns a list of all the items in the world for collision detection"""
        return self.items

    def setup(self):
        """sets up the world with walls, props and items"""
        with open(self.floor, "r") as f:

            csv_reader = csv.reader(f)
            # skips header row
            next(csv_reader, None)

            for row in csv_reader:
                if "wall" in row[0]:
                    self.walls.append(pygame.Rect(float(row[1]), float(row[2]), float(row[3]), float(row[4])))
                elif "prop" in row[0]:
                    self.props.append(Prop(pygame.Vector2(float(row[1]), float(row[2])),pygame.Vector2(float(row[3]), float(row[4]))))
                elif "item" in row[0]:
                    self.items.append(Item(row[0],pygame.Vector2(float(row[1]), float(row[2])), float(row[3])))


    def draw(self, player_pos):
        """draws the walls, props and items to the screen relative to the player's position"""
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

        for item in self.items:
            pygame.draw.circle(screen, "blue",(item.get_pos().x - player_pos.x + screen.get_width() / 2,
                              item.get_pos().y - player_pos.y + screen.get_height() / 2), item.radius)