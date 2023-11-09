# Animation

import pygame
from sys import exit
from random import randint


def display_score():
    global score_surf
    global player_score

    current_time = pygame.time.get_ticks()
    player_score = int(current_time / 1000) - start_time
    score_surf = font.render(f'Score: {player_score}', False, (64, 64, 64)).convert()
    screen.blit(score_surf, score_rect)
    return player_score


def reset_game():
    global player_score
    global start_time
    global obstacle_rect_list
    global game_active
    player_rect.bottom = 300
    player_score = 0
    start_time = int(pygame.time.get_ticks() / 1000)
    obstacle_rect_list = []
    game_active = True


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            if obstacle_rect.bottom == 300:
                screen.blit(snail_surf, obstacle_rect)
            else:
                screen.blit(fly_surf, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.right >= 0]

    return obstacle_list


def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True


def player_animation():
    global player_surf, player_index
    # play walking animation if the player is on floor
    # display the jump surface when the player is not on floor
    if player_rect.bottom < 300:
        # jump anim
        player_surf = player_jump
    else:
        # walk anim
        player_index += 0.1  # passes to next frame gradually
        if player_index >= len(player_walk):
            player_index = 0
        player_surf = player_walk[int(player_index)]  # returns integer index for frame


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
player_walk_1 = pygame.image.load('../graphics/Player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('../graphics/Player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load('../graphics/Player/jump.png').convert_alpha()
player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom=(80, 300))
player_gravity = 0
player_score = 0

# Intro Screen
player_stand = pygame.image.load('../graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))
title_text = font_large.render('Alien Runner', False, (111, 215, 169)).convert()
title_rect = title_text.get_rect(center=(400, 75))
game_message = font_small.render('Press SPACE or click to start!', False, (255, 255, 255))
message_rect = game_message.get_rect(center=(400, 330))

# Score
score_surf = font.render(f'Score: {player_score}', False, (64, 64, 64)).convert()
score_rect = score_surf.get_rect(center=(400, 50))

# Obstacles
snail_frame_1 = pygame.image.load('../graphics/snail/snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('../graphics/snail/snail2.png').convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surf = snail_frames[snail_frame_index]
fly_frame_1 = pygame.image.load('../graphics/Fly/Fly1.png').convert_alpha()
fly_frame_2 = pygame.image.load('../graphics/Fly/Fly2.png').convert_alpha()
fly_frame_index = 0
fly_frames = [fly_frame_1, fly_frame_2]
fly_surf = fly_frames[fly_frame_index]
obstacle_rect_list = []

# Timer
start_time = 0

# Events
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(fly_animation_timer, 200)

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

            if event.type == obstacle_timer:
                if randint(0, 2):
                    obstacle_rect_list.append(snail_surf.get_rect(bottomright=(randint(900, 1100), 300)))
                else:
                    obstacle_rect_list.append(fly_surf.get_rect(bottomright=(randint(900, 1100), 210)))

            if event.type == snail_animation_timer:
                if snail_frame_index == 0:
                    snail_frame_index = 1
                else:
                    snail_frame_index = 0
                snail_surf = snail_frames[snail_frame_index]

            if event.type == fly_animation_timer:
                if fly_frame_index == 0:
                    fly_frame_index = 1
                else:
                    fly_frame_index = 0
                fly_surf = fly_frames[fly_frame_index]

        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    reset_game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    reset_game()

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        pygame.draw.rect(screen, '#c0e8ec', score_rect)
        pygame.draw.rect(screen, '#c0e8ec', score_rect, 6, 6)
        screen.blit(score_surf, score_rect)

        # Player
        player_gravity += 1
        player_rect.bottom += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        player_animation()
        screen.blit(player_surf, player_rect)

        # Obstacle Movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        game_active = collisions(player_rect, obstacle_rect_list)

        # Score
        display_score()

    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(title_text, title_rect)
        if player_score > 0:
            game_message = font_small.render(f'Score: {player_score}', False, (255, 255, 255))
            message_rect = game_message.get_rect(center=(400, 330))
        screen.blit(game_message, message_rect)

    pygame.display.update()
    clock.tick(60)

# Animation
#
# -- Place slightly different looking images in rapid succession
#   -- Player anim: we create our own timer that updates the surface
#   -- Obst. anim: we rely on the inbuild timers to update all obstacle surfaces

# -- Lots of obstacles would create trouble to animate the same way as player.
#   --
