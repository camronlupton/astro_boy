import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else: 
            randomAngle = random.uniform(20, 50)
            vectorOne = self.velocity.rotate(randomAngle)
            vectorTwo = self.velocity.rotate((-1) * randomAngle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            splitOne = Asteroid(self.position.x, self.position.y, new_radius)
            splitOne.velocity = vectorOne * 1.2
            splitTwo = Asteroid(self.position.x, self.position.y, new_radius)
            splitTwo.velocity = vectorTwo * 1.2