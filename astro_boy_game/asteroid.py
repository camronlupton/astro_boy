import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random
import math

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, points=16, noise=0.2, seed=None, rot_speed=30):
        super().__init__(x, y, radius)
        self.rot_deg = 0.0
        self.rot_speed = rot_speed
        self.points = points
        self.noise = noise
        self.seed = seed if seed is not None else random.randrange(1<<30)
        self.verts_local = self._generate_lumpy_polygon((0, 0), radius, points, noise, self.seed)

    def draw(self, screen):
        ang = math.radians(self.rot_deg)
        cos_a, sin_a = math.cos(ang), math.sin(ang)
        # rotate local verts around (0,0), then translate by position
        verts_world = [
            (self.position[0] + x * cos_a - y * sin_a,
             self.position[1] + x * sin_a + y * cos_a)
            for (x, y) in self.verts_local
        ]
        pygame.draw.polygon(screen, "white", verts_world, 2)

    def _generate_lumpy_polygon(self, center, radius, points, noise, seed):
        rnd = random.Random(seed)
        cx, cy = center
        verts = []
        for i in range(points):
            t = (i / points) * 2 * math.pi
            r = radius * (1 + rnd.uniform(-noise, noise))
            x = cx + math.cos(t) * r
            y = cy + math.sin(t) * r
            verts.append((x, y)) 
        return verts



    def update(self, dt):
        self.position += (self.velocity * dt)
        self.rot_deg = (self.rot_deg + self.rot_speed * dt) % 360

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