import pygame

from player.bullet import Bullet

class Player:

    def __init__(self):

        self.width = 50
        self.height = 50

        self.x = 100
        self.y = 300

        self.speed = 5

        self.health = 100

        self.rect = pygame.Rect(
            self.x,
            self.y,
            self.width,
            self.height
        )

        self.bullets = []

        # Shooting Cooldown
        self.shoot_delay = 10

        self.shoot_timer = 0

    def move(self, keys):

        if keys[pygame.K_w]:
            self.rect.y -= self.speed

        if keys[pygame.K_s]:
            self.rect.y += self.speed

        if keys[pygame.K_a]:
            self.rect.x -= self.speed

        if keys[pygame.K_d]:
            self.rect.x += self.speed

    def shoot(self):

        mouse_x, mouse_y = pygame.mouse.get_pos()

        bullet = Bullet(

            self.rect.centerx,
            self.rect.centery,

            mouse_x,
            mouse_y
        )

        self.bullets.append(bullet)

    def auto_shoot(self):

        mouse_buttons = pygame.mouse.get_pressed()

        if mouse_buttons[0]:

            self.shoot_timer += 1

            if self.shoot_timer >= self.shoot_delay:

                self.shoot()

                self.shoot_timer = 0

        else:

            self.shoot_timer = 0

    def update_bullets(self):

        for bullet in self.bullets[:]:

            bullet.move()

            if (
                bullet.rect.x > 1280
                or bullet.rect.x < 0
                or bullet.rect.y > 720
                or bullet.rect.y < 0
            ):

                self.bullets.remove(bullet)

    def draw(self, screen):

        glow_rect = pygame.Rect(
            self.rect.x - 6,
            self.rect.y - 6,
            self.width + 12,
            self.height + 12
        )

        pygame.draw.rect(
            screen,
            (0, 120, 255),
            glow_rect,
            border_radius=12
        )

        pygame.draw.rect(
            screen,
            (0, 255, 255),
            self.rect,
            border_radius=12
        )

        for bullet in self.bullets:
            bullet.draw(screen)