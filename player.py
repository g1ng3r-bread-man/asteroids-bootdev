from circleshape import CircleShape
import pygame
from constants import *
from shots import Shot
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.containers = ()
        self.shotcooldown = 0
        #SUPERDOOPERMEGAULTRARAINBOWMODE!!!!!
        self.rainbowmode = False

        # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def update(self, dt):
        self.shotcooldown -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate((-dt))
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move((-dt))
        if keys[pygame.K_SPACE]:
            self.shoot()
        if keys[pygame.K_3]:
            if self.shotcooldown > 0:
                return
            self.shotcooldown = PLAYER_SHOOT_COOLDOWN
            if self.rainbowmode == False:
                self.rainbowmode = True
            else: self.rainbowmode = False

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shotcooldown > 0:
            return
        self.shotcooldown = PLAYER_SHOOT_COOLDOWN
        newshot = Shot(self.position, SHOT_RADIUS,)
        newshot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED