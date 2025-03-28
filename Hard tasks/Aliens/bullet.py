import pygame as pg
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Класс для управлиння снарядами, якими стриляэ корабель"""

    def __init__(self, ai_game):
        """Створюе об'экт снаряду в поточний позиции корабля"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Створюэмо снаряд в позицийи (0, 0) и призначаемо правильну позицию
        self.rect = pg.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )
        self.rect.midtop = ai_game.ship.rect.midtop

        # Позиція снаряду зберагється як float
        self.y = float(self.rect.y)

    def draw_bullet(self):
        """Виводе снаряд на екран"""
        pg.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        """Перемищуэ снаряд угору по екрану"""
        self.y -= self.settings.bullet_speed_factor
        self.rect.y = self.y