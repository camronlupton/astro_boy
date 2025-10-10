import pygame
from constants import PLAYER_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from circleshape import CircleShape
from shot import Shot


# Base class for game objects
class Player(CircleShape):
    def __init__(self, x, y, shots_group, shot_timer):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shots = shots_group
        self.shot_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        # sub-classes must override
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def reverse(self, dt):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt * (-1)

    def shoot(self):
        if self.shot_timer <= 0:
            shot = Shot(self.position.x, self.position.y)
            direction = pygame.Vector2(0, -1).rotate(self.rotation)
            shot.velocity = direction * PLAYER_SHOOT_SPEED
            self.shots.add(shot) 
            self.shot_timer = PLAYER_SHOOT_COOLDOWN
            

    def update(self, dt):
        self.shot_timer -= dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate((dt * (-1)))
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.reverse(dt)
        if keys[pygame.K_SPACE]:
                self.shoot()

