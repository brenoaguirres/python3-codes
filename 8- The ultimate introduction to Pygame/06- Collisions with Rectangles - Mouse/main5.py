# Collision and Mouse Input

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
player_rect = player_surf.get_rect(midbottom=(80, 300))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEMOTION:  # checking mouse over with event loop
            if player_rect.collidepoint(event.pos):
                print('MOUSE OVER')

        if event.type == pygame.MOUSEBUTTONDOWN:  # printing if button is pressed
            print('mouse down')

        if event.type == pygame.MOUSEBUTTONUP:  # printing if button is released
            print('mouse up')

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (325, 50))

    snail_rect.right -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800
    screen.blit(snail_surf, snail_rect)

    player_rect.left += 1
    screen.blit(player_surf, player_rect)

    if player_rect.colliderect(snail_rect):  # returns 1 for collision, 0 for no collision (False for python)
        print('collision')

    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse_pos):  # receives x, y
        print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)


# Collisions
#   -- rect1.colliderect(rect2)
#   -- rect1.collidepoint((x,y)) - useful for mouse

# Getting mouse position
#   -- pygame.mouse
#   -- event loop

# pygame.mouse or event loop
#   -- mouse position, clicks, buttons, visibility, etc
