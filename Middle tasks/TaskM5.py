import pygame as pg
import random

pg.init()

WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Лови мяч!")

player_img = pg.image.load("Middle tasks\Корзина.bmp")
player_img = pg.transform.scale(player_img, (100, 20))
player = pg.Rect(WIDTH // 2 - 50, HEIGHT - 30, 100, 20)

ball_img = pg.image.load("Middle tasks\мяч.bmp")
ball_img = pg.transform.scale(ball_img, (30, 30))
ball = pg.Rect(random.randint(20, WIDTH - 50), 0, 30, 30)

ball_speed = 5
player_speed = 8

running = True
clock = pg.time.Clock()

while running:
    screen.fill((30, 30, 30))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and player.x > 0:
        player.x -= player_speed
    if keys[pg.K_RIGHT] and player.x < WIDTH - player.width:
        player.x += player_speed

    ball.y += ball_speed

    if ball.y >= HEIGHT:
        ball.x, ball.y = random.randint(20, WIDTH - 50), 0

    if player.colliderect(ball):
        ball.x, ball.y = random.randint(20, WIDTH - 50), 0

    screen.blit(player_img, (player.x, player.y))
    screen.blit(ball_img, (ball.x, ball.y))

    pg.display.flip()
    clock.tick(60)

pg.quit()
