from constants import *
import pygame
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

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return            
        else:
            midangle = random.uniform(20, 50)

            vector1 = self.velocity.rotate(midangle)
            vector2 = self.velocity.rotate(-midangle)
            newradius = self.radius - ASTEROID_MIN_RADIUS

            asteroid1 = Asteroid(self.position.x, self.position.y, newradius, self.colour, self.thickness)
            asteroid1.velocity = vector1 * 1.2

            asteroid2 = Asteroid(self.position.x, self.position.y, newradius, self.colour, self.thickness)
            asteroid2.velocity = vector2 * 1.2

