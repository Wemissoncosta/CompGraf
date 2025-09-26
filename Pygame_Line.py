import pygame
from pygame.locals import *

pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

branco = pygame.Color(255, 255, 255)
cliques_mouse = 0
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            if cliques_mouse == 0:
                ponto1 = pygame.mouse.get_pos()
            else:
                ponto2 = pygame.mouse.get_pos()
            cliques_mouse += 1
            if cliques_mouse > 1:
                pygame.draw.line(screen, branco, ponto1, ponto2, 1)
                cliques_mouse = 0
    pygame.display.update()
pygame.quit()