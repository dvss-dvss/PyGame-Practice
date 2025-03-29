import pygame as pg

from pygame.sprite import Sprite

class Ship(Sprite):
    """Класс для управлиння кораблем"""

    def __init__(self, ai_game):
        """Инициализуэ корабель та встановлюе його початкову позицию"""
        super().__init__()
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Завантаження зобравження корабля и отримання поверхни
        filename = (
            "Hard tasks/Aliens/images/" + "ship-dark.bmp" if self.settings.dark_mode else "ship.bmp"
        )
        self.image = pg.image.load(filename)
        self.rect = self.image.get_rect()
        # Кожен новий корабель з'являэться в нижний чатсини екрану
        self.rect.midbottom = self.screen_rect.midbottom

        # Зберегання дробовойи координати цетра корабля
        self.x = float(self.rect.x)

        # Флаг перемищення
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Рисуэ корабель в поточний позицийи"""
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        """Розміщує корабель внизу екрана"""
        self.rect.midbottom = self.screen_rect.midbottom 
        self.x = float(self.rect.x)  

    def update(self):
        """Оновлюэ позицию корабля з урахування флагу"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed_factor

        # Оновлення атрибуту rect значення self.x
        self.rect.x = self.x