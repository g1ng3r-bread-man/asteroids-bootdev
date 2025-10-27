import pygame
import random
from constants import *
from circleshape import CircleShape
from shots import Shot

class Turret(CircleShape):
    def __init__(self, x, y, asteroids, type):
        super().__init__(x, y, TURRET_RADIUS)
        self.shotcooldown = 0
        self.reload = 0
        self.burst = MACHINE_GUN_BURST_SIZE
        self.containers = ()
        self.rotation = 0.0
        self.asteroids = asteroids
        self.type = type

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def shoot(self):
        if self.shotcooldown > 0:
            return
        if self.type == "normal":
            self.shotcooldown = NORM_TURRET_SHOT_COOLDOWN
            newshot = Shot(self.position, SHOT_RADIUS,)
            newshot.velocity = pygame.Vector2(0,-1).rotate(self.rotation) * TURRET_SHOOT_SPEED

        elif self.type == "shotgun":
            self.shotcooldown = SHOTGUN_TURRET_SHOT_COOLDOWN
            shot1 = Shot(self.position, SHOT_RADIUS)
            shot2 = Shot(self.position, SHOT_RADIUS)
            shot3 = Shot(self.position, SHOT_RADIUS)
            shot1.velocity = pygame.Vector2(-0.33,-1).rotate(self.rotation) * SHOTGUN_TURRET_SHOOT_SPEED
            shot2.velocity = pygame.Vector2(0,-1).rotate(self.rotation) * SHOTGUN_TURRET_SHOOT_SPEED
            shot3.velocity = pygame.Vector2(0.33,-1).rotate(self.rotation) * SHOTGUN_TURRET_SHOOT_SPEED

        elif self.type == "machinegun":
            if self.reload > 0:
                return
            if self.burst > 0:
                self.shotcooldown = max(MACHINE_GUN_MIN_COOLDOWN, MACHINE_GUN_SHOT_COOLDOWN * ((self.burst / 8) / (MACHINE_GUN_BURST_SIZE / 8 )))
                newshot = Shot(self.position, SHOT_RADIUS)
                newshot.velocity = pygame.Vector2(random.choice([x / 10 for x in range(-4, 5)]), -1).rotate(self.rotation) * TURRET_SHOOT_SPEED
                self.burst -= 1
                if self.burst <= 0:
                    self.reload = MACHINE_GUN_RELOAD
                    self.burst = MACHINE_GUN_BURST_SIZE
                    self.shotcooldown = MACHINE_GUN_SHOT_COOLDOWN

        elif self.type == "sniper":
            self.shotcooldown = SNIPER_TURRET_SHOT_COOLDOWN
            newshot = Shot(self.position, SHOT_RADIUS, 2)
            newshot.velocity = pygame.Vector2(0, -1).rotate(self.rotation) * SNIPER_TURRET_SHOOT_SPEED


    def get_target(self):
        if not self.asteroids:
            return None
        try:
            if self.type == "sniper":
                return max(self.asteroids, key=lambda a: self.position.distance_to(a.position))
            else: return min(self.asteroids, key=lambda a: self.position.distance_to(a.position))
        except ValueError:
            return None
        

    def update(self, dt):
        self.shotcooldown = max(0, self.shotcooldown - dt)
        if self.reload > 0:
            self.reload = max(0, self.reload - dt)

        target = self.get_target()
        if not target:
            return
        to_targ = target.position - self.position
        if to_targ.length() == 0:
            return
        
        desiredRot = pygame.Vector2(0,-1).angle_to(to_targ)
        diff = ((desiredRot - self.rotation + 180) % 360) - 180
        max_turn = PLAYER_TURN_SPEED * dt
        turn = max(-max_turn, min(max_turn, diff))
        self.rotation += turn

        if abs(diff) < 6 and self.shotcooldown <= 0:
            self.shoot()

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def draw(self, screen):
        pygame.draw.polygon(screen, "grey", self.triangle(), 3)
