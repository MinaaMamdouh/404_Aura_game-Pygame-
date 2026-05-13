import pygame
import random

from player.player import Player
from enemies.enemy import Enemy
from enemies.boss import Boss

from effects.particle import Particle

from audio.sound_manager import SoundManager

from ui.messages import MessageSystem
from ui.kill_popup import KillPopup
from ui.support_drop import SupportDrop

pygame.init()

pygame.mixer.music.load(
    "assets/music/background.wav"
)

pygame.mixer.music.set_volume(0.3)

pygame.mixer.music.play(-1)

WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("404 aura")

clock = pygame.time.Clock()

# Show Mouse
pygame.mouse.set_visible(True)

font = pygame.font.SysFont("Arial", 36)

big_font = pygame.font.SysFont("Arial", 72)

title_font = pygame.font.SysFont(
    "Arial",
    90,
    bold=True
)

warning_font = pygame.font.SysFont(
    "Arial",
    52,
    bold=True
)

small_font = pygame.font.SysFont(
    "Arial",
    26
)

player = Player()

sound_manager = SoundManager()

message_system = MessageSystem()

boss = None

boss_spawned = False

boss_defeated = False

enemies = []

particles = []

kill_popups = []

support_drops = []

enemy_spawn_timer = 0

support_timer = 0

score = 0

running = True

game_over = False

game_started = False

# Deadline Event
deadline_active = False

deadline_timer = 0


def draw_grid():

    grid_color = (40, 40, 60)

    for x in range(0, WIDTH, 40):

        pygame.draw.line(
            screen,
            grid_color,
            (x, 0),
            (x, HEIGHT)
        )

    for y in range(0, HEIGHT, 40):

        pygame.draw.line(
            screen,
            grid_color,
            (0, y),
            (WIDTH, y)
        )


while running:

    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Start Game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                player.shoot()

                sound_manager.play_shoot()
            if event.key == pygame.K_RETURN:

                game_started = True

            if event.key == pygame.K_r and game_over:

                player.health = 100

                score = 0

                boss = None

                boss_spawned = False

                boss_defeated = False

                enemies.clear()

                particles.clear()

                kill_popups.clear()

                support_drops.clear()

                player.bullets.clear()

                game_over = False

    # MENU
    # MENU
    if not game_started:

        screen.fill((4, 4, 12))

        draw_grid()

        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Background Overlay
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(35)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))

        # Animated Glow
        glow_value = 120 + abs(
            pygame.time.get_ticks() % 120
        )

        # TITLE
        glow_title = title_font.render(
            "404 AURA",
            True,
            (0, glow_value, 255)
        )

        title = title_font.render(
            "404 AURA",
            True,
            (0, 255, 255)
        )

        title_x = WIDTH // 2 - title.get_width() // 2

        screen.blit(glow_title, (title_x + 6, 76))
        screen.blit(title, (title_x, 70))

        # Subtitle
        subtitle = font.render(
            "Cyberpunk Academic Survival",
            True,
            (255, 60, 140)
        )

        subtitle_x = WIDTH // 2 - subtitle.get_width() // 2

        screen.blit(subtitle, (subtitle_x, 185))

        # Main Panel
        panel = pygame.Rect(
            240,
            255,
            800,
            250
        )

        pygame.draw.rect(
            screen,
            (10, 10, 22),
            panel,
            border_radius=24
        )

        pygame.draw.rect(
            screen,
            (0, 255, 255),
            panel,
            2,
            border_radius=24
        )

        # Lore Text
        lore1 = small_font.render(
            "The university system has been corrupted.",
            True,
            (255, 255, 255)
        )

        lore2 = small_font.render(
            "Defeat corrupted TAs and survive endless deadlines.",
            True,
            (255, 255, 255)
        )

        lore3 = small_font.render(
            "Professor.exe is the final boss of the system.",
            True,
            (255, 80, 80)
        )

        lore4 = small_font.render(
            "Eng.Menna provides support boosts during battle.",
            True,
            (0, 255, 120)
        )

        # Center Text
        lore1_x = WIDTH // 2 - lore1.get_width() // 2
        lore2_x = WIDTH // 2 - lore2.get_width() // 2
        lore3_x = WIDTH // 2 - lore3.get_width() // 2
        lore4_x = WIDTH // 2 - lore4.get_width() // 2

        # Draw Text
        screen.blit(lore1, (lore1_x, 305))
        screen.blit(lore2, (lore2_x, 355))
        screen.blit(lore3, (lore3_x, 405))
        screen.blit(lore4, (lore4_x, 455))

        # Small Cyberpunk Lines
        pygame.draw.line(
            screen,
            (0, 255, 255),
            (470, 342),
            (810, 342),
            2
        )

        pygame.draw.line(
            screen,
            (0, 255, 255),
            (420, 392),
            (860, 392),
            2
        )

        # Controls
        controls = small_font.render(
            "WASD = Move | Mouse = Aim | SPACE / Hold Left Click = Shoot",
            True,
            (255, 210, 60)
        )

        controls_x = WIDTH // 2 - controls.get_width() // 2

        screen.blit(controls, (controls_x, 545))

        # START BUTTON
        start_button = pygame.Rect(
            500,
            610,
            280,
            65
        )

        hovered = start_button.collidepoint(
            mouse_x,
            mouse_y
        )

        if hovered:

            button_color = (0, 255, 255)

            if pygame.mouse.get_pressed()[0]:
                game_started = True

        else:

            button_color = (0, 180, 255)

        pygame.draw.rect(
            screen,
            button_color,
            start_button,
            border_radius=18
        )

        pygame.draw.rect(
            screen,
            (255, 255, 255),
            start_button,
            2,
            border_radius=18
        )

        # Button Text
        start_text = font.render(
            "START GAME",
            True,
            (5, 5, 15)
        )

        start_x = (
                start_button.x
                + start_button.width // 2
                - start_text.get_width() // 2
        )

        screen.blit(start_text, (start_x, 625))

        # Credits
        credits = small_font.render(
            "Made by Mina Mamdouh & A'laa Madeh",
            True,
            (0, 255, 120)
        )

        credits_x = WIDTH // 2 - credits.get_width() // 2

        screen.blit(credits, (credits_x, 695))

        pygame.display.update()

        continue

    # GAMEPLAY
    if not game_over:

        enemy_spawn_timer += 1

        if enemy_spawn_timer > 60 and not boss_spawned:

            enemies.append(Enemy())

            enemy_spawn_timer = 0

        # Spawn Support
        support_timer += 1

        if support_timer > 600:

            support_drops.append(
                SupportDrop()
            )

            support_timer = 0

    # Spawn Boss
    if score >= 20 and not boss_spawned:

        boss = Boss()

        boss_spawned = True

    # Deadline Timer
    deadline_timer += 1

    if deadline_timer > 900:

        deadline_active = True

    if deadline_timer > 1200:

        deadline_active = False

        deadline_timer = 0

    # Instant Mouse Shooting
    mouse_buttons = pygame.mouse.get_pressed()

    if mouse_buttons[0] and not game_over:

        player.auto_shoot()

        sound_manager.play_shoot()

    if not game_over:

        keys = pygame.key.get_pressed()

        player.move(keys)

        player.update_bullets()

        message_system.update()

        # Enemy Movement
        for enemy in enemies[:]:

            if deadline_active:
                enemy.rect.x -= enemy.speed + 3

            else:
                enemy.move()

            if enemy.rect.x < -100:
                enemies.remove(enemy)

        # Boss Movement
        if boss and boss.health > 0:

            boss.move(player)

        # Support Collision
        for support in support_drops[:]:

            if player.rect.colliderect(
                support.rect
            ):

                player.health += 20

                if player.health > 100:
                    player.health = 100

                support_messages = [

                    "Eng.Menna saved your GPA 💙",

                    "Eng.Menna leaked the assignment answers 👀",

                    "Eng.Menna distracted the TA 😭",

                    "Eng.Menna extended the deadline 🔥",

                    "Eng.Menna activated emergency support ⚡",

                    "Eng.Menna hacked the grading system 👾",

                    "Eng.Menna boosted your motivation 💻",

                    "Eng.Menna protected you from Professor.exe 🛡️"

                ]

                kill_popups.append(

                    KillPopup(
                        random.choice(
                            support_messages
                        ),
                        support.rect.x,
                        support.rect.y
                    )

                )

                support_drops.remove(support)

        # Bullet Collision
        for bullet in player.bullets[:]:

            # Enemy Collision
            for enemy in enemies[:]:

                if bullet.rect.colliderect(enemy.rect):

                    if bullet in player.bullets:
                        player.bullets.remove(bullet)

                    if enemy in enemies:
                        enemies.remove(enemy)

                    sound_manager.play_hit()

                    score += 1

                    popup_texts = [

                        "+100 AURA 🔥",
                        "NICE SHOT 😈",
                        "TA DESTROYED 💀",
                        "ASSIGNMENT DEFENDED ✅",
                        "GPA SAVED 😭",
                        "ACADEMIC SURVIVAL +1",
                        "FINAL BOSS ENERGY ⚡"

                    ]

                    kill_popups.append(

                        KillPopup(
                            random.choice(popup_texts),
                            enemy.rect.x,
                            enemy.rect.y
                        )

                    )

                    for i in range(15):

                        particles.append(
                            Particle(
                                enemy.rect.centerx,
                                enemy.rect.centery
                            )
                        )

                    break

            # Boss Collision
            if boss and bullet.rect.colliderect(
                boss.rect
            ):

                if bullet in player.bullets:
                    player.bullets.remove(bullet)

                boss.health -= 1

                sound_manager.play_hit()

                for i in range(20):

                    particles.append(
                        Particle(
                            boss.rect.centerx,
                            boss.rect.centery
                        )
                    )

                if boss.health <= 0:

                    boss_defeated = True

        # Boss Damage
        if boss and player.rect.colliderect(
            boss.rect
        ):

            player.health -= 1

            if player.health <= 0:

                sound_manager.play_game_over()

                game_over = True

        # Player Damage
        for enemy in enemies[:]:

            if player.rect.colliderect(enemy.rect):

                enemies.remove(enemy)

                player.health -= 10

                if player.health <= 0:

                    sound_manager.play_game_over()

                    game_over = True

        # Particle Updates
        for particle in particles[:]:

            particle.update()

            if particle.life <= 0:
                particles.remove(particle)

        # Popup Updates
        for popup in kill_popups[:]:

            popup.update()

            if popup.life <= 0:
                kill_popups.remove(popup)

    # Background
    screen.fill((10, 10, 20))

    draw_grid()

    # Deadline Red Overlay
    if deadline_active:

        overlay = pygame.Surface(
            (WIDTH, HEIGHT)
        )

        overlay.set_alpha(60)

        overlay.fill((255, 0, 0))

        screen.blit(overlay, (0, 0))

    # Draw Player
    player.draw(screen)

    # Draw Enemies
    for enemy in enemies:
        enemy.draw(screen)

    # Draw Boss
    if boss and boss.health > 0:

        boss.draw(screen)

    # Draw Support Drops
    for support in support_drops:
        support.draw(screen)

    # Draw Particles
    for particle in particles:
        particle.draw(screen)

    # Draw Kill Popups
    for popup in kill_popups:
        popup.draw(screen)

    # Meme Messages
    message_system.draw(screen)

    # Boss Warning
    if boss and boss.health > 0:

        boss_text = warning_font.render(
            "Professor.exe has entered the chat 💀",
            True,
            (255, 0, 0)
        )

        screen.blit(
            boss_text,
            (170, 80)
        )

    # Boss Defeated
    if boss_defeated:

        win_text = big_font.render(
            "YOU SURVIVED THE FINAL 😭🔥",
            True,
            (0, 255, 120)
        )

        screen.blit(win_text, (100, 320))

    # Deadline Warning
    if deadline_active:

        warning_text = warning_font.render(
            "⚠ DEADLINE APPROACHING ⚠",
            True,
            (255, 50, 50)
        )

        screen.blit(warning_text, (270, 40))

    # Score UI
    score_text = font.render(
        f"SCORE: {score}",
        True,
        (0, 255, 255)
    )

    screen.blit(score_text, (20, 20))

    # Health UI
    health_text = font.render(
        f"HEALTH: {player.health}",
        True,
        (255, 50, 50)
    )

    screen.blit(health_text, (20, 70))

    # Game Over Screen
    if game_over:

        game_over_text = big_font.render(
            "YOU FAILED THE COURSE",
            True,
            (255, 0, 0)
        )

        restart_text = font.render(
            "Press R to Restart",
            True,
            (255, 255, 255)
        )

        screen.blit(game_over_text, (180, 300))
        screen.blit(restart_text, (470, 400))

    pygame.display.update()

pygame.quit()