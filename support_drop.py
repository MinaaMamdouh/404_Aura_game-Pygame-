import pygame
import random

class SupportDrop:

    def __init__(self):

        self.width = 40
        self.height = 40

        self.x = random.randint(300, 1100)
        self.y = random.randint(100, 600)

        self.rect = pygame.Rect(
            self.x,
            self.y,
            self.width,
            self.height
        )

        self.active = True

    def draw(self, screen):

        glow_rect = pygame.Rect(
            self.rect.x - 6,
            self.rect.y - 6,
            self.width + 12,
            self.height + 12
        )

        pygame.draw.rect(
            screen,
            (0, 150, 255),
            glow_rect,
            border_radius=12
        )

        pygame.draw.rect(
            screen,
            (100, 220, 255),
            self.rect,
            border_radius=12
        )