import pygame

class SoundManager:

    def __init__(self):

        pygame.mixer.init()

        self.shoot_sound = pygame.mixer.Sound(
            "assets/sounds/shoot.wav"
        )

        self.hit_sound = pygame.mixer.Sound(
            "assets/sounds/hit.wav"
        )

        self.game_over_sound = pygame.mixer.Sound(
            "assets/sounds/game_over.wav"
        )

        self.shoot_sound.set_volume(0.3)
        self.hit_sound.set_volume(0.4)
        self.game_over_sound.set_volume(0.5)

    def play_shoot(self):

        self.shoot_sound.play()

    def play_hit(self):

        self.hit_sound.play()

    def play_game_over(self):

        self.game_over_sound.play()