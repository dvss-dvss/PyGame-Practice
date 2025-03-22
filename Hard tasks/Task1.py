import pygame as pg

pg.init()

WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Космічний корабель")

ship_img = pg.image.load("Hard tasks\ship.bmp")
ship_img = pg.transform.scale(ship_img, (100, 50))
ship = pg.Rect(WIDTH // 2 - 50, HEIGHT - 80, 100, 50)

ship_speed = 8
game_active = False

font = pg.font.Font(None, 36)
clock = pg.time.Clock()

while True:
    screen.fill((255, 255, 255))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_p:
                game_active = True  

    if not game_active:
        text = font.render("Натисни P, щоб почати", True, (0, 0, 0))
        screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2))
        pg.display.flip()
        continue  

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and ship.x > 0:
        ship.x -= ship_speed
    if keys[pg.K_RIGHT] and ship.x < WIDTH - ship.width:
        ship.x += ship_speed

    screen.blit(ship_img, (ship.x, ship.y))
    pg.display.flip()
    clock.tick(60)
