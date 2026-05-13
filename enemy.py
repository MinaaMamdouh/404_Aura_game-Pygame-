import pygame
import random

class Enemy:

    def __init__(self):

        self.width = 50
        self.height = 50

        self.x = random.randint(900, 1200)
        self.y = random.randint(50, 650)

        self.speed = random.randint(2, 5)

        self.rect = pygame.Rect(
            self.x,
            self.y,
            self.width,
            self.height
        )

    def move(self):

        self.rect.x -= self.speed

    def draw(self, screen):

        glow_rect = pygame.Rect(
            self.rect.x - 6,
            self.rect.y - 6,
            self.width + 12,
            self.height + 12
        )

        pygame.draw.rect(
            screen,
            (255, 0, 100),
            glow_rect,
            border_radius=12
        )

        pygame.draw.rect(
            screen,
            (255, 50, 120),
            self.rect,
            border_radius=12
        )