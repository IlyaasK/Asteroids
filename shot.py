from circleshape import CircleShape
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen,"white", self.position, self.radius)


    def update(self, dt):
        self.position += (self.velocity * dt)

    def rotate(self, player):
        self.rotation = player.rotation
