import pygame
from sys import exit

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))  # create display surface
clock = pygame.time.Clock()  # create clock

while True:
    # exiting game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()  # updates display surface
    clock.tick(60)  # controls FPS

