from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_angle = random.uniform(20, 50)
        new_asteroid1 = Asteroid(self.position[0], self.position[1], self.radius / 2)
        new_asteroid2 = Asteroid(self.position[0], self.position[1], self.radius / 2)
        new_asteroid1.velocity = self.velocity.rotate(new_angle) * 1.2
        new_asteroid2.velocity = self.velocity.rotate(-new_angle) * 1.2
