import pygame

class Boss:

    def __init__(self):

        self.width = 140
        self.height = 140

        self.x = 1000
        self.y = 250

        self.speed = 3

        self.health = 30

        self.rect = pygame.Rect(
            self.x,
            self.y,
            self.width,
            self.height
        )

    def move(self, player):

        if self.rect.x > player.rect.x:
            self.rect.x -= self.speed

        if self.rect.y < player.rect.y:
            self.rect.y += self.speed

        if self.rect.y > player.rect.y:
            self.rect.y -= self.speed

    def draw(self, screen):

        glow_rect = pygame.Rect(
            self.rect.x - 10,
            self.rect.y - 10,
            self.width + 20,
            self.height + 20
        )

        pygame.draw.rect(
            screen,
            (255, 0, 0),
            glow_rect,
            border_radius=20
        )

        pygame.draw.rect(
            screen,
            (255, 60, 60),
            self.rect,
            border_radius=20
        )

        # Boss HP Bar
        pygame.draw.rect(
            screen,
            (60, 60, 60),
            (390, 20, 500, 30)
        )

        pygame.draw.rect(
            screen,
            (255, 0, 0),
            (390, 20, self.health * 16, 30)
        )