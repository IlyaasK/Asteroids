from circleshape import CircleShape
import pygame
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen,"white", self.position, self.radius)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self): 
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            ast1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            ast2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            ast1.velocity = self.velocity.rotate(random.uniform(20, 50)) * SPEED_MULTIPLIER
            ast2.velocity = self.velocity.rotate(-(random.uniform(20, 50))) * SPEED_MULTIPLIER




            
