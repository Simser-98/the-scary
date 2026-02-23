import pygame


class Item:
    """a class for items in the world that the player can interact with"""
    def __init__(self, item_id, world_pos, radius):
        """initializes the item with an id, position and radius for interaction"""
        self.itemId = item_id
        self.worldPos = world_pos
        self.radius = radius

    def get_id(self):
        """getter for the item id"""
        return self.itemId

    def get_pos(self):
        """getter for the position of the prop"""
        return self.worldPos

    def get_radius(self):
        """getter for the dimensions of the prop"""
        return self.radius

    def check_distance(self, player_pos, player_radius):
        """checks if the prop is within radius of player"""
        vector_magnitude = pygame.Vector2.length(player_pos - self.worldPos)

        return vector_magnitude < player_radius + self.radius

