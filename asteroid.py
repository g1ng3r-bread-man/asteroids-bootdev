from constants import *
import random
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, colour, thickness):
        super().__init__(x, y, radius)
        self.radius = radius
        self.colour = colour
        self.colourlist = ("white", "green", "blue", "yellow", "red", "pink", "brown")
        self.thickness = thickness
        #RAINBOWMODE!!!!!!!!!!
        self.rainbow = False
        #Different coloured asteroids
        self.diffcolours = False

    def draw(self, screen):
        if self.rainbow == True:
            pygame.draw.circle(screen, random.choice(self.colourlist), self.position, self.radius, self.thickness)
        elif self.diffcolours == True:
            pygame.draw.circle(screen, self.colour, self.position, self.radius, self.thickness)
        else: pygame.draw.circle(screen, "white", self.position, self.radius, self.thickness)

    def update(self, dt):
        self.position += (self.velocity * dt)
    