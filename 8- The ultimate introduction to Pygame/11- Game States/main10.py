# Game States

import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

game_active = True

font = pygame.font.Font('../font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('../graphics/Sky.png').convert()
ground_surface = pygame.image.load('../graphics/ground.png').convert()

score_surf = font.render('Runner', False, (64, 64, 64)).convert()
score_rect = score_surf.get_rect(center=(400, 50))

snail_surf = pygame.image.load('../graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom=(600, 300))

player_surf = pygame.image.load('../graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (player_rect.collidepoint(event.pos)
                        and event.button == pygame.BUTTON_LEFT):
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE
                        and player_rect.bottom >= 300):
                    player_gravity = -20
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:        # resetting game if not game_active
                if event.button == pygame.BUTTON_LEFT:
                    player_rect.bottom = 300
                    snail_rect.left = 800
                    game_active = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_rect.bottom = 300
                    snail_rect.left = 800
                    game_active = True

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        pygame.draw.rect(screen, '#c0e8ec', score_rect)
        pygame.draw.rect(screen, '#c0e8ec', score_rect, 6, 6)
        screen.blit(score_surf, score_rect)

        # Snail
        snail_rect.right -= 4
        if snail_rect.right <= 0:
            snail_rect.left = 800
        screen.blit(snail_surf, snail_rect)

        # Player
        player_gravity += 1
        player_rect.bottom += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        # Collision
        if player_rect.colliderect(snail_rect):
            game_active = False
    else:                                                   # stopping game if not game_active
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))

    pygame.display.update()
    clock.tick(60)

# Game State and Game Over State
# Implemented reset
