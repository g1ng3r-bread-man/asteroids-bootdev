from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, piercing_val=0):
        super().__init__(x, y, SHOT_RADIUS)
        self.containers = ()
        self.piercing = piercing_val
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 5)

    def update(self, dt):
        self.position += (self.velocity * dt)
        buffer = SHOT_RADIUS + 2
        if (self.position.x < -buffer or 
        self.position.x > SCREEN_WIDTH + buffer or 
        self.position.y < -buffer or 
        self.position.y > SCREEN_HEIGHT + buffer):
            self.kill()