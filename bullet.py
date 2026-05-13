import pygame
import math

class Bullet:

    def __init__(self, x, y, target_x, target_y):

        self.width = 12
        self.height = 12

        self.speed = 15

        self.rect = pygame.Rect(
            x,
            y,
            self.width,
            self.height
        )

        # Direction Vector
        dx = target_x - x
        dy = target_y - y

        distance = math.sqrt(dx ** 2 + dy ** 2)

        if distance != 0:

            self.dx = dx / distance
            self.dy = dy / distance

        else:

            self.dx = 0
            self.dy = 0

    def move(self):

        self.rect.x += self.dx * self.speed
        self.rect.y += self.dy * self.speed

    def draw(self, screen):

        glow_rect = pygame.Rect(
            self.rect.x - 4,
            self.rect.y - 4,
            self.width + 8,
            self.height + 8
        )

        pygame.draw.ellipse(
            screen,
            (255, 100, 100),
            glow_rect
        )

        pygame.draw.ellipse(
            screen,
            (255, 0, 0),
            self.rect
        )