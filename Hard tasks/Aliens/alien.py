import pygame as pg
from pygame.sprite import Sprite


class Alien(Sprite):
    """Класс для прибульця"""

    def __init__(self, ai_game):
        """Инициалицуе прибульця та задае його позицию"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Завантаження зображення та вызначення rect
        filename = (
            "Hard tasks/Aliens/images/" + "alien-dark.bmp" if self.settings.dark_mode else "alien.bmp"
        )
        self.image = pg.image.load(filename)
        self.rect = self.image.get_rect()

        # Кошен новий прибулець з'являеться в ливому верхньому кути екрану
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Збереження точної горизонтальної позиції прибульця
        self.x = float(self.rect.x)

    def chek_edges(self):
        """Повертає True, якщо прибулець біля краю екрана"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <=0:
            return True

    def update(self):
        """Переміщує прибульця праворуч"""
        self.x += self.settings.alien_speed_factor * self.settings.fleet_direction
        self.rect.x = self.x
