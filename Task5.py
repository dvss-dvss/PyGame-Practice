import pygame as pg
import sys

pg.init()

screen_width, screen_height = 800, 600
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Ship")

background_color = (30, 30, 30)

ship = pg.image.load('rocket.bmp')
ship_width, ship_height = 100, 100
ship = pg.transform.scale(ship, (ship_width, ship_height))
ship_rect = ship.get_rect(midleft=(50, screen_height // 2))
ship_speed = 5

bullet_radius = 6
bullet_speed = 2
bullets = []

can_shoot = True

running = True
while running:
    screen.fill(background_color)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and can_shoot:
                bullets.append([ship_rect.right, ship_rect.centery])
                can_shoot = False
        if event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:
                can_shoot = True

    keys = pg.key.get_pressed()
    if keys[pg.K_UP]:
        ship_rect.y -= ship_speed
    if keys[pg.K_DOWN]:
        ship_rect.y += ship_speed

    ship_rect.y = max(0, min(screen_height - ship_height, ship_rect.y))

    for bullet in bullets[:]:
        bullet[0] += bullet_speed
        if bullet[0] > screen_width:  
            bullets.remove(bullet)

    screen.blit(ship, ship_rect)
    for bullet in bullets:
        pg.draw.circle(screen, (255, 0, 0), (bullet[0], bullet[1]), bullet_radius)

    pg.display.flip()

pg.quit()
sys.exit()
