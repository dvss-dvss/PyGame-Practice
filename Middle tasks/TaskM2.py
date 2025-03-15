import pygame as pg
import sys
import random

pg.init()

screen_width, screen_height = 800, 600
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Star Grid")

background_color = (0, 0, 0)

star = pg.image.load('Middle tasks\star.bmp')
star_size = 50
star = pg.transform.scale(star, (star_size, star_size))

rows, cols = 8, 10
padding = 20

start_x = (screen_width - (cols * (star_size + padding) - padding)) // 2
start_y = (screen_height - (rows * (star_size + padding) - padding)) // 2


star_positions = []
for row in range(rows):
    for col in range(cols):
        offset_x = random.randint(-10, 10)
        offset_y = random.randint(-10, 10)
        x = start_x + col * (star_size + padding) + offset_x
        y = start_y + row * (star_size + padding) + offset_y
        star_positions.append((x, y))


running = True
while running:
    screen.fill(background_color)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

 
    for pos in star_positions:
        screen.blit(star, pos)

    pg.display.flip()


pg.quit()
sys.exit()
