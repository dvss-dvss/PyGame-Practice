import sys
from time import sleep

import pygame as pg

from alien import Alien
from bullet import Bullet
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard
from settings import Settings
from ship import Ship
from star import Star


class AlienInvasion:
    """Класс для управлиння ресурсами та повединкою гри"""

    def __init__(self):
        """Инициализуэ гру та створюе игрови ресурси"""
        pg.init()
        self.settings = Settings()

        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pg.display.set_caption("Alien Invasion")

        # Створення екземпляра для зберігання ігрової статистики
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.stars = pg.sprite.Group()
        for _ in range(self.settings.star_limit):
            self.stars.add(Star(self))

        self.ship = Ship(self)
        self.bullets = pg.sprite.Group()
        self.aliens = pg.sprite.Group()

        self._create_fleet()

        # Створення кнопок
        self.play_button = Button(self, "Play")
        self.pause_buttonn = Button(self, "Pause")

    def _check_aliens_bottom(self):
         """Перевіряє, чи досягли прибульці нижнього краю екрана"""
         screen_rect = self.screen.get_rect()
         for alien in self.aliens.sprites():
             if alien.rect.bottom >= screen_rect.bottom:
                 self._ship_hit()
                 break

    def _check_bullet_alien_collisions(self):
        """Обробляє колізії снарядів х прибульцями"""
        # Перевірка потраплянь у прибульців
        collisions = pg.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prepare_score()
            self.sb.check_high_score() 

        if not self.aliens:
            # Знищення існуючих снарядів та створення нового флоту
            self.bullets.empty()
            self._create_fleet() 
            self.settings.increase_speed()

            # Збильшення ривня
            self.stats.level += 1
            self.sb.prepare_level

    def _chek_events(self):
        """Обробляэ натиснення клавиш та подйи миши"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                    self._check_keydown_events(event)
            elif event.type == pg.KEYUP:
                self._check_keyup_events(event)

            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keyup_events(self, event):
        if event.key == pg.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pg.K_LEFT:
            self.ship.moving_left = False

    def _change_fleet_direction(self):
        """Опускае весь флот та звинюе напрям руху"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_fleet_edges(self):
        """Реагуе на досягненя прибульця краю екрана"""
        for alien in self.aliens.sprites():
            if alien.chek_edges():
                self._change_fleet_direction()
                break

    def _check_keydown_events(self, event):
        if event.key == pg.K_RIGHT:
                # Перемищуэмо корабель праворуч
                self.ship.moving_right = True
        elif event.key == pg.K_LEFT:
                self.ship.moving_left = True
        elif event.key == pg.K_ESCAPE:
            sys.exit()
        elif event.key == pg.K_SPACE and not self.stats.game_paused:
            self._fire_bullet()
        elif event.key == pg.K_RETURN:
             if not self.stats.game_active:
                 self._start_new_game()
             else:
                 self.stats.game_paused = not self.stats.game_paused

    def _check_play_button(self, mouse_pos):
        """Запускає нову гру коли натиснуто кнопку Play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self._start_new_game()

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(alien)

    def _create_fleet(self):
        """Створюе флот прибульцив"""
        # Створення прибульця и вызначення килькости прибульцив в ряду
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - 2 * alien_width
        number_aliens_x = available_space_x // (2 * alien_width)
 
        # Визначення кількості рядів
        ship_height = self.ship.rect.height
        available_space_y = (
            self.settings.screen_height - (3 * alien_height) - ship_height
        )
        number_rows = available_space_y // (2 * alien_height)
 
        # Створення флоту прибульців
        for row_number in range(number_rows):
            # Створення ряду прибульців
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _fire_bullet(self):
        """Створюе новий снаряд та додаэ його до групи"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _ship_hit(self):
        """Обробляє зіткнення корабля з прибульцем"""
        if self.stats.ships_left > 0:
            # Зменшення ships_left
            self.stats.ships_left -= 1
            self.sb.prepare_ships()

            # Очщення списків прибульців та снарядів
            self.aliens.empty()
            self.bullets.empty()

            # Створення нового флоту та центрування корабля
            self._create_fleet()
            self.ship.center_ship()

            # Пауза
            sleep(0.5)

        else:
            self.stats.game_active = False
            pg.mouse.set_visible(True)

    def _start_new_game(self):
        """Запускае нову гру"""
        # Скидання ігрової статистики та налштувань
        self.settings.initialize_dynamic_setting()
        self.stats.reset_stats()
        self.stats.game_active = True
        self.sb.prepare_score()
        self.sb.prepare_level()
        self.sb.prepare_ships()

        # Очистка списків прибульців та снарядів
        self.aliens.empty()
        self.bullets.empty()
 
        # Створення нового флоту та розміщення корабля по центру
        self._create_fleet()
        self.ship.center_ship()

        # Приховати мишу
        pg.mouse.set_visible(False)

    def _update_aliens(self):
        """Оновлює позиції всіх прибульців флоту"""
        self._check_fleet_edges()
        self.aliens.update()

    def _update_bullets(self):
        """Оновлює позиції снарядів"""
        self.bullets.update()
        #print(len(self.bullets))

        # Перевірка колізій "прибулець-корабель"
        if pg.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_bottom()

        # Видалення снарядів, що вилетіли за край екрану
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)          

        self._check_bullet_alien_collisions()

    def _update_screen(self):
        """Оновлюэ зображення на екрани та видображаэ новий екран"""
        self.screen.fill(self.settings.bg_color)
        self.stars.update()
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Виведення інформації про результати
        self.sb.show_score()

        # Кнопка Play відображається, коли гра неактивна
        if not self.stats.game_active:
            self.play_button.draw_button()
        elif self.stats.game_paused:
            self.pause_buttonn.draw_button()

        # Відображення останнього прорисованого екрану
        pg.display.flip()

    def run_game(self):
        """Запуск основного циклу гри"""
        while True:
            #Видслидкування подий клавиатури та миши
            self._chek_events()
            if self.stats.game_active and not self.stats.game_paused:
                 self.ship.update()
                 self._update_bullets()
                 self._update_aliens()
            self._update_screen()

if __name__ == '__main__':
    # Створення екземпляру та запуск гри
    ai = AlienInvasion()
    ai.run_game()
