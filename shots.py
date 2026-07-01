from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius=SHOT_RADIUS, piercing_val=0):
        super().__init__(x, y, radius)
        self.containers = ()
        self.piercing = piercing_val
        self.radius = SHOT_RADIUS
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 5)

    def update(self, dt):
        self.position += (self.velocity * dt)
        buffer = self.radius + 2
        if (self.position.x < -buffer or 
        self.position.x > SCREEN_WIDTH + buffer or 
        self.position.y < -buffer or 
        self.position.y > SCREEN_HEIGHT + buffer):
            self.kill()