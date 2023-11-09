# Transforming Surfaces

import pygame
from sys import exit


def display_score():
    global score_surf
    global player_score

    current_time = pygame.time.get_ticks()
    player_score = int(current_time / 1000) - start_time
    score_surf = font.render(f'Score: {player_score}', False, (64, 64, 64)).convert()
    screen.blit(score_surf, score_rect)
    return player_score


# Window
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

# Game logic
game_active = False

# Text
font = pygame.font.Font('../font/Pixeltype.ttf', 50)
font_large = pygame.font.Font('../font/Pixeltype.ttf', 75)
font_small = pygame.font.Font('../font/Pixeltype.ttf', 25)

# Background
sky_surface = pygame.image.load('../graphics/Sky.png').convert()
ground_surface = pygame.image.load('../graphics/ground.png').convert()

# Player
player_surf = pygame.image.load('../graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))
player_gravity = 0
player_score = 0

# Intro Screen
player_stand = pygame.image.load('../graphics/Player/player_stand.png').convert_alpha()
# player_stand_scaled = pygame.transform.scale(player_stand, (200, 400))        # basic scaling
# player_stand = pygame.transform.scale2x(player_stand)                           # 2x scaling
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)         # rotate and scale, apply filter
player_stand_rect = player_stand.get_rect(center=(400, 200))
title_text = font_large.render('Alien Runner', False, (111, 215, 169)).convert()
title_rect = title_text.get_rect(center=(400, 75))
game_message = font_small.render('Press SPACE or click to start!', False, (255, 255, 255))
message_rect = game_message.get_rect(center=(400, 330))

# Score
score_surf = font.render(f'Score: {player_score}', False, (64, 64, 64)).convert()
score_rect = score_surf.get_rect(center=(400, 50))

# Snail
snail_surf = pygame.image.load('../graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom=(600, 300))

# Timer
start_time = 0

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (player_rect.collidepoint(event.pos)
                        and event.button == pygame.BUTTON_LEFT
                        and player_rect.bottom >= 300):
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
                    player_score = 0
                    start_time = int(pygame.time.get_ticks() / 1000)
                    game_active = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_rect.bottom = 300
                    snail_rect.left = 800
                    player_score = 0
                    start_time = int(pygame.time.get_ticks() / 1000)
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

        # Score
        display_score()

        # Collision
        if player_rect.colliderect(snail_rect):
            game_active = False
    else:                                                   # stopping game if not game_active
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(title_text, title_rect)
        if player_score > 0:
            game_message = font_small.render(f'Score: {player_score}', False, (255, 255, 255))
            message_rect = game_message.get_rect(center=(400, 330))
        screen.blit(game_message, message_rect)

    pygame.display.update()
    clock.tick(60)

# Transform Surfaces
#   -- Move, Rotate, Scale surfaces

#   Methods to scale:
#   pygame.transform.scale()
#   pygame.transform.rotozoom()  # takes surface, angle, scale
#   pygame.transform.scale2x()
#   pygame.transform.smoothscale()

#   -- Displaying the score in the game over screen.
#   1) We store the score in a function
#   2) current_time needs to be global or be returned
#   3) place the returned score on a surface and blit it
