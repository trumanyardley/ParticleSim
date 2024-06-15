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

#Cooldown timer to slowdown rate of particle placement
cooldown_timer = 0
cooldown_duration = 5 #decrease this to increase speed of placement

#Control amount of particles being placed on cursor
placement_size = 1

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
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP and placement_size < 6:
            placement_size += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and placement_size > 1:
            placement_size -= 1
        elif particle_type != "Water" and event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            particle_type = "Water"
        elif particle_type != "Sand" and event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            particle_type = "Sand"
        elif particle_type != "Stone" and event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            particle_type = "Stone"

    if cooldown_timer > 0:
        cooldown_timer -= 1


    # Assuming this is within your main loop
    if pygame.mouse.get_pressed()[0] and cooldown_timer == 0:
        x, y = pygame.mouse.get_pos()
        curr_row = int(y / PARTICLE_DIMENSION)
        curr_col = int(x / PARTICLE_DIMENSION)

        # Calculate the range for rows and columns based on placement_size
        offset = placement_size - 1

        # Iterate over the square area centered around the cursor position
        for row_offset in range(-offset, offset + 1):
            for col_offset in range(-offset, offset + 1):
                # Calculate the row and column for the current cell in the loop
                target_row = curr_row + row_offset
                target_col = curr_col + col_offset

                # Check if the target cell is within the bounds of the grid
                if 0 <= target_row < len(cells) and 0 <= target_col < len(cells[0]):
                    # Place the particle based on the current particle type
                    if particle_type == "Sand":
                        cells[target_row][target_col] = Sand(target_row, target_col)
                    elif particle_type == "Water":
                        cells[target_row][target_col] = Water(target_row, target_col)
                    elif particle_type == "Stone":
                        cells[target_row][target_col] = Stone(target_row, target_col)

        # Reset the cooldown timer after placing particles
        cooldown_timer = cooldown_duration

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
    
    #Display current particle type under fps
    particle_text = font.render(particle_type, True, pygame.Color("white"))
    screen.blit(particle_text, (SCREEN_WIDTH - particle_text.get_width() - 10, 50))

    #Display cursor highlight
    x, y = pygame.mouse.get_pos()
    #pygame.draw.rect(screen, (255, 87,51), (int(x / PARTICLE_DIMENSION) * PARTICLE_DIMENSION, int(y / PARTICLE_DIMENSION) * PARTICLE_DIMENSION, PARTICLE_DIMENSION, PARTICLE_DIMENSION), width=2)

    # Assuming PARTICLE_DIMENSION is the size of a single particle
    # and placement_size determines the size of the placement area

    # Calculate the top-left corner of the highlight area
    highlight_size = 1 + (placement_size - 1) * 2  # Calculate the total highlight size based on placement_size
    offset = (placement_size - 1) * PARTICLE_DIMENSION  # Calculate the offset from the cursor position

    # Adjust the position to start from the top-left corner of the highlight area
    highlight_x = int(x / PARTICLE_DIMENSION) * PARTICLE_DIMENSION - offset
    highlight_y = int(y / PARTICLE_DIMENSION) * PARTICLE_DIMENSION - offset

    # Draw the highlight rectangle with the adjusted size
    pygame.draw.rect(screen, (255, 87, 51), (highlight_x, highlight_y, PARTICLE_DIMENSION * highlight_size, PARTICLE_DIMENSION * highlight_size), width=2)
    # flip() the display to put your work on screen
    pygame.display.flip()

    #fps
    clock.tick(60)



pygame.quit()
