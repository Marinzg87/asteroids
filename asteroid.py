from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.radius = radius
    
    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="white", radius=self.radius, width=2)