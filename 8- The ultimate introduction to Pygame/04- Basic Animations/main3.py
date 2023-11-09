# Basic Animations

import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

font = pygame.font.Font('../font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('../graphics/Sky.png').convert()  # .convert() converts png to format common to pygame
ground_surface = pygame.image.load('../graphics/ground.png').convert()
text_surface = font.render('Runner', False, 'Black').convert()

snail_surface = pygame.image.load('../graphics/snail/snail1.png').convert_alpha()  # converts preserving alpha channel
snail_x_pos = 600

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (325, 50))

    snail_x_pos -= 4  # moving snail 4px left each frame
    if snail_x_pos <= -100:  # resetting snail x-pos
        snail_x_pos = 800
    screen.blit(snail_surface, (snail_x_pos, 265))  # updating snail placement position each time
    pygame.display.update()
    clock.tick(60)


# Basic Animations
# -- Draw each frame a different image or position - illusion of movement
# -- Use variable containing the position change
