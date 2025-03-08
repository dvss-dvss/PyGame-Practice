import pygame as pg
import sys

# Инициализация pg
pg.init()

# Настройки экрана
screen_width, screen_height = 800, 600
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Rocket Game")

# Цвет фона
background_color = (30, 30, 30)

# Загружаем ракету
rocket = pg.image.load('ship.bmp')
rocket_width, rocket_height = 100, 100
rocket = pg.transform.scale(rocket, (rocket_width, rocket_height))

# Начальное положение ракеты (по центру)
rocket_rect = rocket.get_rect(center=(screen_width // 2, screen_height // 2))

# Скорость движения ракеты
rocket_speed = 2

# Основной игровой цикл
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Получаем состояние клавиш
    keys = pg.key.get_pressed()

    # Движение ракеты
    if keys[pg.K_UP]:
        rocket_rect.y -= rocket_speed
    if keys[pg.K_DOWN]:
        rocket_rect.y += rocket_speed
    if keys[pg.K_LEFT]:
        rocket_rect.x -= rocket_speed
    if keys[pg.K_RIGHT]:
        rocket_rect.x += rocket_speed

    # Ограничения, чтобы ракета не вылетала за границы экрана
    rocket_rect.x = max(0, min(screen_width - rocket_width, rocket_rect.x))
    rocket_rect.y = max(0, min(screen_height - rocket_height, rocket_rect.y))

    # Отрисовка
    screen.fill(background_color)
    screen.blit(rocket, rocket_rect)
    pg.display.flip()

# Завершение игры
pg.quit()
sys.exit()
