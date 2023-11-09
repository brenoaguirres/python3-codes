# Player - Keyboard Input

import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

font = pygame.font.Font('../font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('../graphics/Sky.png').convert()
ground_surface = pygame.image.load('../graphics/ground.png').convert()

score_surf = font.render('Runner', False, (64, 64, 64)).convert()
score_rect = score_surf.get_rect(center=(400, 50))

snail_surf = pygame.image.load('../graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom=(600, 300))

player_surf = pygame.image.load('../graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('key down')

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                print('key up')

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 6, 6)
    screen.blit(score_surf, score_rect)

    snail_rect.right -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800
    screen.blit(snail_surf, snail_rect)
    screen.blit(player_surf, player_rect)

    keys = pygame.key.get_pressed()  # keyboard input
    if keys[pygame.K_SPACE]:
        print('Jump')

    pygame.display.update()
    clock.tick(60)


# Player - Keyboard Input
#   -- 1) keyboard
#   -- 2) Jump + gravity
#   -- 3) creating a floor

# Keyboard Input
#   -- Pygame.key
#   -- event loop

# Two input Types
#   -- event loop is proper for general stuff - e.g. closing the game
#   -- pygame.mouse and pygame.keys are useful for working with classes

