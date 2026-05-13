import pygame
import random

class MessageSystem:

    def __init__(self):

        self.messages = [

            "Where is the assignment? 😈",
            "bro is cooked 💀",
            "This will be in the final 🙂",
            "skill issue.",
            "Review the sessions again.",
            "Deadline approaching 😭",
            "GPA corrupted.",
            "ERROR 404: Motivation not found.",
            "The code crashed 💀",
            "The TA is watching you 👁️",
            "No bugs detected (big lie).",
            "Academic danger level rising ⚠",
            "System overload detected.",
            "You forgot the documentation 😭",
            "Professor.exe is getting closer."

        ]

        self.current_message = ""

        self.message_timer = 0

        self.font = pygame.font.SysFont(
            "Arial",
            34,
            bold=True
        )

    def update(self):

        self.message_timer += 1

        if self.message_timer > 240:

            self.current_message = random.choice(
                self.messages
            )

            self.message_timer = 0

    def draw(self, screen):

        if self.current_message != "":

            text = self.font.render(
                self.current_message,
                True,
                (255, 50, 120)
            )

            bg_rect = pygame.Rect(
                260,
                120,
                760,
                60
            )

            pygame.draw.rect(
                screen,
                (20, 20, 30),
                bg_rect,
                border_radius=12
            )

            pygame.draw.rect(
                screen,
                (255, 0, 120),
                bg_rect,
                3,
                border_radius=12
            )

            screen.blit(
                text,
                (290, 135)
            )