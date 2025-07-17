import pygame
from constants import *


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        from player import Player
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collisioncheck(self, player):
        if pygame.Vector2.distance_to(self.position, player.position) <= self.radius + player.radius:
            return True
        return False