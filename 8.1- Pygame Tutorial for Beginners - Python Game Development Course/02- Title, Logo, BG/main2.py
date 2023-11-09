# Changing Title, Logo, BG

import pygame
from sys import exit

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))  # create display surface
clock = pygame.time.Clock()  # create clock

# Title and Icon
icon = pygame.image.load('../16- Game Over/images/logo.png').convert_alpha()
pygame.display.set_caption('Space Invaders')
pygame.display.set_icon(icon)

while True:
    # event loop
    #   -- exit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((0, 0, 0))  # painting black the BG

    pygame.display.update()  # updates display surface
    clock.tick(60)  # controls FPS

