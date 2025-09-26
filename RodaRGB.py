import pygame
pygame.init()
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))


done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    for y in range (500):
        for x in range (500):
            screen.set_at((x, y),
            pygame.Color (int (x/screen_width * 255), int(y/screen_height * 255), 255))
    pygame.display.update()
pygame.quit()