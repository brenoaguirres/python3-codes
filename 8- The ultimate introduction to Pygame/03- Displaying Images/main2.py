# Displaying Images

import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

font = pygame.font.Font('../font/Pixeltype.ttf', 50)  # create font obj (type/path, size)

test_surface = pygame.Surface((100, 200))     # creates a surface with w, h
test_surface.fill('Red')     # fill with color - named-colors, (r, g, b, a)

sky_surface = pygame.image.load('../graphics/Sky.png')    # loads an image
ground_surface = pygame.image.load('../graphics/ground.png')
text_surface = font.render('Runner', False, 'Black')  # create text surface (text, AA, color)


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))   # block image transfer - (surface, (xpos, ypos))
    screen.blit(ground_surface, (0, 300))  # renders in order of calls
    screen.blit(text_surface, (325, 50))
    pygame.display.update()
    clock.tick(60)


# Surfaces (python)
# -- Display Surface
#       The game window. Displays other stuff.
# -- (regular) Surface
#       Essentially a single image (something imported, rendered text or plain color).
#       Needs to be displayed on DS.

# (0, 0) - top-left
