import pygame as pg
import sys

pg.init()

screen_width, screen_height = 1000, 700
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Ракета")

background_color = (30, 30, 30)
screen.fill(background_color)


character = pg.image.load('rocket.bmp')
character = pg.transform.scale(character, (300, 300))
character_rect = character.get_rect(center=(screen_width // 2, screen_height // 2))


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill(background_color)  
    screen.blit(character, character_rect)  
    pg.display.flip()

pg.quit()
sys.exit()
