# Better Spawn Logic - Timers - Custom Events

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
    print(obstacles)
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True


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
snail_surf = pygame.image.load('../graphics/snail/snail1.png').convert_alpha()
fly_surf = pygame.image.load('../graphics/Fly/Fly1.png').convert_alpha()
obstacle_rect_list = []

# Timer
start_time = 0

# Timer Event
obstacle_timer = pygame.USEREVENT + 1  # add new event reference to avoid conflict with pygame reserved events
pygame.time.set_timer(obstacle_timer, 1500)  # call the event continuously in 'ms' milliseconds

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

            if event.type == obstacle_timer:  # everytime the event happens append a rectangle in randint distance
                if randint(0, 2):  # 1 True // 0 False
                    obstacle_rect_list.append(snail_surf.get_rect(bottomright=(randint(900, 1100), 300)))
                else:
                    obstacle_rect_list.append(fly_surf.get_rect(bottomright=(randint(900, 1100), 210)))

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

# Better Spawn Logic
#
#   Timers
#   1) Create a custom event
#   2) Tell pygame to trigger that event continuously
#   3) Add code in the event loop

# New Obstacle Logic
#   1) Create a list of obstacle rectangles
#   2) Everytime the timer triggers we add a new rectangle to that list
#   3) We Move every rectangle in that list to the left on every frame
#   4) We delete rectangles too far left

# Problems
#   1) Collisions doesn't work anymore
#   2) Objects aren't being deleted after screen - List Comprehension elegant solution

# Implementing different spawns - Fly
#   1) Import the fly
