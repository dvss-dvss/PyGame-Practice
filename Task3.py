import pygame as pg
import sys


pg.init()


screen_width, screen_height = 800, 600
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Rocket Game")


background_color = (31, 31, 31)


rocket = pg.image.load('ship.bmp')
rocket_width, rocket_height = 100, 100
rocket = pg.transform.scale(rocket, (rocket_width, rocket_height))


rocket_rect = rocket.get_rect(center=(screen_width // 2, screen_height // 2))


rocket_speed = 2


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


    keys = pg.key.get_pressed()


    if keys[pg.K_UP]:
        rocket_rect.y -= rocket_speed
    if keys[pg.K_DOWN]:
        rocket_rect.y += rocket_speed
    if keys[pg.K_LEFT]:
        rocket_rect.x -= rocket_speed
    if keys[pg.K_RIGHT]:
        rocket_rect.x += rocket_speed


    rocket_rect.x = max(0, min(screen_width - rocket_width, rocket_rect.x))
    rocket_rect.y = max(0, min(screen_height - rocket_height, rocket_rect.y))


    screen.fill(background_color)
    screen.blit(rocket, rocket_rect)
    pg.display.flip()

pg.quit()
sys.exit()
