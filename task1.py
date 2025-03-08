import pygame as pg
import sys

pg.init()

WIDTH, HEIGHT = 1300, 700
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Синє небо")

BLUE = (255, 255, 255)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    screen.fill(BLUE)
    
    pg.display.flip()

pg.quit()
sys.exit()