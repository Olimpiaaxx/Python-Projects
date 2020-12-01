# Pygame template - skeleton for a new pygame project
import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 204, 204)
COLOURS = [WHITE, BLACK, RED, GREEN, BLUE]

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()


pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('Sylan + Olimpia = <3', False, (0, 0, 0))

i = 5
j = 5
text_pos_x = 0
text_pos_y = 0


# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # process input (events)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                text_pos_x -= 1

    # Update

    # Draw / render
    screen.fill(PINK)
    screen.blit(textsurface,(text_pos_x, text_pos_y))
    #text_pos_x += i
    #text_pos_y += j
    if (text_pos_x + 270)>= WIDTH or text_pos_x <= 0:
        i = -i
    if (text_pos_y + 40) >= HEIGHT or text_pos_y <= 0:
        j = -j

    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
