import pygame
pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

#def inverter_cordenadas (display, x ,y):
    #return x, display.get_height() - y

done = False
branco = pygame.Color(255, 255, 255)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #screen.set_at(inverter_cordenadas(screen, 100, 100), branco)
    #screen.set_at(inverter_cordenadas(screen, 200, 200), branco)
    position = [100, 100]
    pygame.draw.rect(screen, branco, (position[0], position[1], 80, 80))
    pygame.display.update()
pygame.quit()