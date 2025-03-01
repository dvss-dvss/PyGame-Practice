import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 1300, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Синє небо")

BLUE = (0, 0, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(BLUE)
    
    pygame.display.flip()

pygame.quit()
sys.exit()


