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
        self.current_shoot_cooldown = PLAYER_SHOOT_COOLDOWN
        #SUPERDOOPERMEGAULTRARAINBOWMODE!!!!!
        self.rainbowmode = False
        self.carmode = True
        self.degreeAngle = (self.rotation+0.001)%360
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

    def draw(self, screen):
        self.degreeAngle = (self.rotation+0.001)%360
        if self.carmode:
            if self.degreeAngle > 157.5 and self.degreeAngle < 202.5:
                screen.blit(ncar, (self.position.x-24, self.position.y-24))
            if self.degreeAngle > 112.5 and self.degreeAngle < 157.5:
                screen.blit(nwcar, (self.position.x-24, self.position.y-24))
            if self.degreeAngle > 67.5 and self.degreeAngle < 112.5:
                screen.blit(wcar, (self.position.x-24, self.position.y-24))
            if self.degreeAngle > 22.5 and self.degreeAngle < 67.5:
                screen.blit(swcar, (self.position.x-24, self.position.y-24))
            if self.degreeAngle >= 0 and self.degreeAngle < 22.5:
                screen.blit(scar, (self.position.x-24, self.position.y-24))
            if self.degreeAngle > 337.5 and self.degreeAngle <= 360:
                screen.blit(scar, (self.position.x-24, self.position.y-24))
            if self.degreeAngle > 292.5 and self.degreeAngle < 337.5:
                screen.blit(secar, (self.position.x-24, self.position.y-24))
            if self.degreeAngle > 247.5 and self.degreeAngle < 292.5:
                screen.blit(ecar, (self.position.x-24, self.position.y-24))
            if self.degreeAngle > 202.5 and self.degreeAngle < 247.5:
                screen.blit(necar, (self.position.x-24, self.position.y-24))
        else:    
            pygame.draw.polygon(screen, "white", self.triangle(), 2)

        

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
        if keys[pygame.K_q]:
            self.shoot(True)
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

    def shoot(self, bigshot=False):
        if self.shotcooldown > 0:
            return
        if not bigshot:
            self.shotcooldown = self.current_shoot_cooldown
            newshot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            newshot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        elif bigshot:
            self.shotcooldown = self.current_shoot_cooldown
            newshot = Shot(self.position.x, self.position.y, 30, 200)
            newshot.velocity = pygame.Vector2(0,0.4).rotate(self.rotation) * PLAYER_SHOOT_SPEED
