# Rectangles

import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

font = pygame.font.Font('../font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('../graphics/Sky.png').convert()
ground_surface = pygame.image.load('../graphics/ground.png').convert()
text_surface = font.render('Runner', False, 'Black').convert()

snail_surf = pygame.image.load('../graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom=(600, 300))

player_surf = pygame.image.load('../graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))  # Create rectangle for player based on player surface

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (325, 50))

    snail_rect.right -= 4
    if snail_rect.right <= 0:  # checks if it is out of screen.
        snail_rect.left = 800  # must position its left point on 800 otherwise it'll appear onscreen.
    screen.blit(snail_surf, snail_rect)

    player_rect.left += 1  # updating via rectangle and not via surface
    screen.blit(player_surf, player_rect)

    pygame.display.update()
    clock.tick(60)


# Rectangles
# -- Precise positioning of surfaces
# -- Basic collisions
#       - Tuple (x,y)
#       - points - top, topleft, midtop, topright, center, midleft, midright, left, right, (centerx, centery)
#               (x,y), bottomleft, midbottom, bottom, bottomright

