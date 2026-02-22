import pygame

class Prop:
    def __init__(self, world_pos, dimensions):
        self.worldPos = world_pos
        self.dimensions = dimensions

    def get_pos(self):
        """getter for the position of the prop"""
        return self.worldPos

    def get_dimensions(self):
        """getter for the dimensions of the prop"""
        return self.dimensions