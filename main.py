# Example file showing a basic pygame "game loop"
import pygame
import numpy as np
from particle import *
from sand import *
from water import *
from stone import *

#Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BRUSH_RADIUS = 3

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

#Determine given screen dimensions what grid will be
max_rows = int(SCREEN_HEIGHT / PARTICLE_DIMENSION)
max_cols = int(SCREEN_WIDTH / PARTICLE_DIMENSION)

#array of cells that track where particles are on the screen
# cells = np.zeros((max_rows, max_cols))
#all particles currently existing on screen
# particles = []

font = pygame.font.SysFont("Arial", 36)

particle_type = "Sand"

cells = [[None for _ in range(max_cols)] for _ in range(max_rows)]



while running:
    pause = True
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif particle_type != "Water" and event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            particle_type = "Water"
        elif particle_type != "Sand" and event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            particle_type = "Sand"
        elif particle_type != "Stone" and event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            particle_type = "Stone"


    #Place particle when mouse is pressed down
    if pygame.mouse.get_pressed()[0]:
        x, y = pygame.mouse.get_pos()
        curr_row = int(y / PARTICLE_DIMENSION)
        curr_col = int(x / PARTICLE_DIMENSION)
        if particle_type == "Sand":
            cells[curr_row][curr_col] = Sand(curr_row, curr_col) 
        elif particle_type == "Water":
            cells[curr_row][curr_col] = Water(curr_row, curr_col)
        elif particle_type == "Stone":
            cells[curr_row][curr_col] = Stone(curr_row, curr_col)


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    #Draw and update particles on screen
    for row in range(max_rows - 1, -1,-1):
        for col in range(max_cols):
            particle = cells[row][col]
            if particle is not None:
                particle.update(cells)
                particle.draw(screen)


    #Display fps in top right corner
    fps = round(clock.get_fps(), 1)
    fps_string = "FPS: {}".format(fps)
    fps_text = font.render(fps_string, True, pygame.Color("white"))
    screen.blit(fps_text, (SCREEN_WIDTH - fps_text.get_width() - 10, 10))

    # flip() the display to put your work on screen
    pygame.display.flip()

    #fps
    clock.tick(60)



pygame.quit()
