import os
import pygame as pg


class GameStats:
    """Відслідковування статистики гри"""
 
    def __init__(self, ai_game):
        """Ініціалізує статистику"""
        self.settings = ai_game.settings
        self.reset_stats()

        self.game_active = False

        self.high_score = 0

    def reset_stats(self):
        """Іеіціалізує статистику, що змінюється під час гри"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

FILENAME = "high_score.txt"

    def load_high_score():
        """Загружает рекорд из файла, если он существует"""
        if os.path.exists(FILENAME):
            with open(FILENAME, "r") as file:
                return int(file.read().strip())
        else:
            return 0 

    def save_high_score(score):
        """Сохраняет рекорд в файл"""
        with open(FILENAME, "w") as file:
            file.write(str(score))  

    high_score = load_high_score()

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False  

        score = 100  

        if score > high_score:
            high_score = score
            save_high_score(high_score)


