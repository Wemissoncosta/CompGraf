import pygame

pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

branco = pygame.Color(255, 255, 255)
pygame.font.init()
fonte = pygame.font.SysFont('arial', 120, False, True)
texto = fonte.render('Wemisson Costa', False, branco)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(texto, (10, 10))

    pygame.display.update()
pygame.quit()