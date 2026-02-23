import pygame

class Prop:
    """class for props in the world, which are
    non-collidable objects that can be drawn to the screen"""
    def __init__(self, world_pos, dimensions):
        """initializes the prop with a position and dimensions"""
        self.worldPos = world_pos
        self.dimensions = dimensions

    def get_pos(self):
        """getter for the position of the prop"""
        return self.worldPos

    def get_dimensions(self):
        """getter for the dimensions of the prop"""
        return self.dimensions