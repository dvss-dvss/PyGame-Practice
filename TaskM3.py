import pygame as pg
import random

pg.init()

WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Дождь")

drop_img = pg.image.load("капля.bmp")

drop_width, drop_height = drop_img.get_size()

cols = WIDTH // (drop_width + 10)
rows = HEIGHT // (drop_height + 30)

drops = []
for i in range(cols):
    for j in range(rows):
        x = i * (drop_width + 10)
        y = j * (drop_height + 30) - HEIGHT 
        speed = random.uniform(2, 5) 
        drops.append({"x": x, "y": y, "speed": speed})


running = True
clock = pg.time.Clock()

while running:
    screen.fill((0, 0, 0))  

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    for drop in drops:
        drop["y"] += drop["speed"]

        screen.blit(drop_img, (drop["x"], drop["y"]))

    pg.display.flip()
    clock.tick(60)

pg.quit()

