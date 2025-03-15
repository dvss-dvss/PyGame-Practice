import pygame as pg
import sys

pg.init()

screen_width, screen_height = 800, 600
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Key Event Logger")

background_color = (0, 0, 0)

running = True
while running:
    screen.fill(background_color)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            print(f"Key pressed: {event.key}")
    
    pg.display.flip()

pg.quit()
sys.exit()
