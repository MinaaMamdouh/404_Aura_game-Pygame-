import pygame
import random

class Particle:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.size = random.randint(3, 7)

        self.speed_x = random.randint(-4, 4)
        self.speed_y = random.randint(-4, 4)

        self.life = 30

        self.color = (
            random.randint(150, 255),
            0,
            random.randint(100, 255)
        )

    def update(self):

        self.x += self.speed_x
        self.y += self.speed_y

        self.life -= 1

    def draw(self, screen):

        pygame.draw.circle(
            screen,
            self.color,
            (int(self.x), int(self.y)),
            self.size
        )