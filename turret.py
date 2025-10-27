import pygame
from constants import *
from circleshape import CircleShape
from shots import Shot

class Turret(CircleShape):
    def __init__(self, x, y, asteroids):
        super().__init__(x, y, TURRET_RADIUS)
        self.shotcooldown = 0
        self.containers = ()
        self.rotation = 0.0
        self.asteroids = asteroids

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
        self.shotcooldown = TURRET_SHOT_COOLDOWN
        newshot = Shot(self.position, SHOT_RADIUS,)
        newshot.velocity = pygame.Vector2(0,-1).rotate(self.rotation) * TURRET_SHOOT_SPEED
    
    def get_target(self):
        if not self.asteroids:
            return None
        try:
            return min(self.asteroids, key=lambda a: self.position.distance_to(a.position))
        except ValueError:
            return None
        

    def update(self, dt):
        self.shotcooldown -= dt

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
