import pygame

from object import *


class Player(Object):
    def __init__(self):
        super().__init__()
        self._worldPos = pygame.Vector2(0, 0)

    def get_pos(self):
        return self._worldPos

    def tick(self, keys, delta_time):
        if keys[pygame.K_w]:
            self._worldPos.y -= 1 * delta_time
        if keys[pygame.K_s]:
            self._worldPos.y += 1 * delta_time
        if keys[pygame.K_a]:
            self._worldPos.x -= 1 * delta_time
        if keys[pygame.K_d]:
            self._worldPos.x += 1 * delta_time
        print(self._worldPos)
