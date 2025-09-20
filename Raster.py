import pygame


pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Raster")
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(fundo, (0, 0))
    screen.blit(sprite, (100, 100))

    pygame.display.update()
pygame.quit()