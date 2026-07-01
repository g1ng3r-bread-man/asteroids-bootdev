from constants import *
import pygame
import random
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius, colour, thickness, upgrade, speed=0):
        super().__init__(x, y, radius)
        self.radius = radius
        self.isUpgrade = upgrade
        self.shotcooldown = 0
        self.colour = colour
        self.colourlist = ("white", "green", "blue", "yellow", "red", "pink", "brown")
        self.thickness = thickness
        #RAINBOWMODE!!!!!!!!!!
        self.rainbow = False
        #Different coloured asteroids
        self.diffcolours = False
        self.homing = True
        self.speed = speed
        self.rotation = 0
        self.nextbot = random.choice([obunga, klein, sanic, gargitron, armstrong])

    def draw(self, screen):
        if self.homing:
            screen.blit(self.nextbot, (self.position.x-24, self.position.y-24))
            return
        if self.rainbow == True:
            pygame.draw.circle(screen, random.choice(self.colourlist), self.position, self.radius, self.thickness)
        elif self.diffcolours == True:
            pygame.draw.circle(screen, self.colour, self.position, self.radius, self.thickness)
        elif self.isUpgrade == True:
            pygame.draw.circle(screen, random.choice(self.colourlist), self.position, self.radius, 20)
        else: pygame.draw.circle(screen, "white", self.position, self.radius, self.thickness)

    def update(self, dt, target):
        self.shotcooldown -= dt
        if self.homing:
            self.position += self.home(300, dt, target)
        else:
            self.position += (self.velocity * dt)
        buffer = ASTEROID_MAX_RADIUS + 2
        if (self.position.x < -buffer or 
        self.position.x > SCREEN_WIDTH + buffer or 
        self.position.y < -buffer or 
        self.position.y > SCREEN_HEIGHT + buffer):
            self.kill()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            if self.shotcooldown > 0:
                return
            self.shotcooldown = PLAYER_SHOOT_COOLDOWN
            if self.diffcolours == False:
                self.diffcolours = True
            else: self.diffcolours = False
        if keys[pygame.K_2]:
            if self.shotcooldown > 0:
                return
            self.shotcooldown = PLAYER_SHOOT_COOLDOWN
            if self.rainbow == False:
                self.rainbow = True
            else: self.rainbow = False

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return            
        else:
            midangle = random.uniform(20, 50)

            vector1 = self.velocity.rotate(midangle)
            vector2 = self.velocity.rotate(-midangle)
            newradius = self.radius - ASTEROID_MIN_RADIUS

            asteroid1 = Asteroid(self.position.x, self.position.y, newradius, self.colour, self.thickness, 0)
            asteroid1.velocity = vector1 * 1.2

            asteroid2 = Asteroid(self.position.x, self.position.y, newradius, self.colour, self.thickness, 0)
            asteroid2.velocity = vector2 * 1.2

    def home(self, turnSpeed, dt, target=None):
        if target is None:
            return pygame.Vector2(0,0)
        to_targ = target.position - self.position
        if to_targ.length() == 0:
            return pygame.Vector2(0,0)
        desiredRot = pygame.Vector2(0,-1).angle_to(to_targ)
        diff = ((desiredRot - self.rotation + 180) % 360) - 180
        max_turn = turnSpeed * dt
        turn = max(-max_turn, min(max_turn, diff))
        self.rotation += turn
        direction = pygame.Vector2(0, -1).rotate(self.rotation)
        self.velocity = direction * self.speed
        return self.velocity * dt