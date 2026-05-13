import pygame

class KillPopup:

    def __init__(self, text, x, y):

        self.text = text

        self.x = x
        self.y = y

        self.life = 60

        self.font = pygame.font.SysFont(
            "Arial",
            28,
            bold=True
        )

    def update(self):

        self.y -= 1

        self.life -= 1

    def draw(self, screen):

        render = self.font.render(
            self.text,
            True,
            (0, 255, 120)
        )

        screen.blit(
            render,
            (self.x, self.y)
        )