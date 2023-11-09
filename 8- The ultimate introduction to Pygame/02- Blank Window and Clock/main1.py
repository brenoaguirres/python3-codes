import pygame
from sys import exit

# starts pygame functionalities, like render, sounds, etc
# starting the engine of the car
pygame.init()
screen = pygame.display.set_mode((800, 400))    # Create the surface with (w, h)
pygame.display.set_caption('Runner')    # title and optional icon
clock = pygame.time.Clock()

while True:  # game loop
    # receive input
    # update logic
    # draw elements

    for event in pygame.event.get():  # returns all events in pygame
        if event.type == pygame.QUIT:
            pygame.quit()   # de-initializes everything
            exit()  # exit game loop and python code

    pygame.display.update()  # updates display surface
    clock.tick(60)  # tells to run max 60 fps (wait 1/60 seconds on the current frame)

# Controlling the frame rate
# -- Frame rate independency (constant)
#       * Game runs equally on each hardware
#       * Ceiling (60 FPS)
#           easy to tell PC to pause between frames
#           - clock object
#       * Floor (60 FPS)
#           hard. requires game optimization for pretended hardware
#           - never too much on screen for example.
