import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_WIDTH
from constants import ASTEROID_SPLIT_MIN_ANGLE
from constants import ASTEROID_SPLIT_MAX_ANGLE
from constants import ASTEROID_MIN_RADIUS
from constants import ASTEROID_SPLIT_VELOCITY_MULTIPLAYER

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, ASTEROID_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        new_angle = random.uniform(ASTEROID_SPLIT_MIN_ANGLE, ASTEROID_SPLIT_MAX_ANGLE)
        new_velocity1 = self.velocity.rotate(new_angle) * ASTEROID_SPLIT_VELOCITY_MULTIPLAYER
        new_velocity2 = self.velocity.rotate(-new_angle) * ASTEROID_SPLIT_VELOCITY_MULTIPLAYER
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = new_velocity1

        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2.velocity = new_velocity2

