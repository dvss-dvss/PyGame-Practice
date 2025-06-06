class Settings:
    """Класс для збригання всих налаштувань гри"""

    def __init__(self):
       #Параметри екрану
       self.screen_width = 1300
       self.screen_height = 700
       self.dark_mode = True
       self.bg_color = (0, 0, 0) if self.dark_mode else (230, 230, 230)

       # Параметри корабля
       self.ship_limit = 3

       # Параметри снаряду
       self.bullet_width = 3
       self.bullet_height = 15
       self.bullet_color = (255, 0, 0) if self.dark_mode else (60, 60, 60)
       self.bullets_allowed = 3

       # Параметри прибульців
       self.fleet_drop_speed = 10

       # Параметри зірок
       self.star_limit = 100
       self.star_speed = 0.5
       self.star_start_color = 200
       self.star_color_limit = 256
       self.star_color_step = 0.15
       self.star_radius = 3

       # Темп пришвидшення гри
       self.speedup_scale = 1.1
       self.score_scale = 1.5

       self.initialize_dynamic_setting()

    def initialize_dynamic_setting(self):
        """Ініціалізує налаштування, що змінюються під час гри"""
        self.ship_speed_factor = 3
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1.5

        # fleet_direction = 1 якщо флот рухається праворуч, -1 якщо ліворуч
        self.fleet_direction = 1

        # Підрахунок очок
        self.alien_points = 50

    def increase_speed(self):
        """Збільшує налаштування швидкості"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)