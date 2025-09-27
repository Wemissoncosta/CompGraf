import pygame
from pygame.locals import *
from OpenGL.GL  import *
from OpenGL.GLU import *
from Cubo import*


pygame.init()
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF|OPENGL)

pygame.display.set_caption('Inicio OpenGL')

done = False
branco = (255,255,255)
gluPerspective(30, (screen_width/screen_height), 0.1, 100.0)
glTranslatef(0.0,0.0,-3)

malha = Cubo()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glRotatef(1,0,1,0)
    malha.desenhar()
    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()