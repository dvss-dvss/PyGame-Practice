import pygame as pg
import random

pg.init()

WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Космічна стрілялка")

ship_img = pg.image.load("Hard tasks\ship.bmp")
ship_img = pg.transform.scale(ship_img, (50, 50))
ship = pg.Rect(50, HEIGHT // 2 - 25, 50, 50)

bullet_speed = 10
target_speed = 5
ship_speed = 8

bullets = []
missed = 0
game_active = False

font = pg.font.Font(None, 36)
play_button = pg.Rect(WIDTH // 2 - 50, HEIGHT // 2 - 25, 100, 50)

# Мишень
target = pg.Rect(WIDTH - 70, random.randint(50, HEIGHT - 100), 50, 50)
target_direction = 1

clock = pg.time.Clock()

keys = {pg.K_UP: False, pg.K_DOWN: False}

while True:
    screen.fill((255, 255, 255))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

        if event.type == pg.KEYDOWN:
            if game_active:
                if event.key in keys:
                    keys[event.key] = True
                if event.key == pg.K_SPACE:
                    bullets.append(pg.Rect(ship.x + ship.width, ship.y + 20, 10, 5))
            else:
                if event.key == pg.K_p:
                    game_active = True
                    missed = 0
                    bullets.clear()

        if event.type == pg.KEYUP:
            if event.key in keys:
                keys[event.key] = False

        if event.type == pg.MOUSEBUTTONDOWN:
            if not game_active and play_button.collidepoint(event.pos):
                game_active = True
                missed = 0
                bullets.clear()

    if not game_active:
        pg.draw.rect(screen, (0, 255, 0), play_button)
        text = font.render("Play", True, (0, 0, 0))
        screen.blit(text, (WIDTH // 2 - 20, HEIGHT // 2 - 10))
        pg.display.flip()
        continue

    target.y += target_speed * target_direction
    if target.top <= 0 or target.bottom >= HEIGHT:
        target_direction *= -1

    if keys[pg.K_UP] and ship.y > 0:
        ship.y -= ship_speed
    if keys[pg.K_DOWN] and ship.y < HEIGHT - ship.height:
        ship.y += ship_speed

    for bullet in bullets[:]:
        bullet.x += bullet_speed
        if bullet.colliderect(target):
            bullets.remove(bullet)
            target.y = random.randint(50, HEIGHT - 100)
        elif bullet.x > WIDTH:
            bullets.remove(bullet)
            missed += 1
            if missed >= 3:
                game_active = False

    screen.blit(ship_img, (ship.x, ship.y))
    pg.draw.rect(screen, (255, 0, 0), target)
    for bullet in bullets:
        pg.draw.rect(screen, (0, 0, 255), bullet)

    text = font.render(f"Пропущено: {missed}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    pg.display.flip()
    clock.tick(60)

