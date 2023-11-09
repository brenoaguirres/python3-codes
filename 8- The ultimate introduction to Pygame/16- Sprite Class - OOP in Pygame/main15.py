# Sprite and OOP
import random

import pygame
from sys import exit
from random import randint, choice


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # anim
        player_walk_1 = pygame.image.load('../graphics/Player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('../graphics/Player/player_walk_2.png').convert_alpha()
        self.player_jump = pygame.image.load('../graphics/Player/jump.png').convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0

        self.image = self.player_walk[self.player_index]  # surface
        self.rect = self.image.get_rect(midbottom=(80, 300))  # rect
        self.gravity = 0
        self.score = 0

    def player_input(self):
        mouse = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20

        if pygame.BUTTON_LEFT in mouse and self.rect.bottom >= 300:
            self.gravity = -20

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self, *args, **kwargs):
        self.player_input()
        self.apply_gravity()
        self.animation_state()


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, obs_type):
        super().__init__()

        if obs_type == 'fly':
            fly_1 = pygame.image.load('../graphics/Fly/Fly1.png').convert_alpha()
            fly_2 = pygame.image.load('../graphics/Fly/Fly2.png').convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 210
            self.speed = 4
        else:
            snail_1 = pygame.image.load('../graphics/snail/snail1.png').convert_alpha()
            snail_2 = pygame.image.load('../graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 300
            self.speed = 4

        # anim
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(bottomright=(randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[self.animation_index]

    def destroy(self):
        if self.rect.right <= 0:
            self.kill()

    def movement(self):
        self.rect.x -= self.speed

    def update(self, *args, **kwargs):
        self.destroy()
        self.animation_state()
        self.movement()


def display_score():
    global score_surf
    global player_score

    current_time = pygame.time.get_ticks()
    player_score = int(current_time / 1000) - start_time
    score_surf = font.render(f'Score: {player_score}', False, (64, 64, 64)).convert()
    screen.blit(score_surf, score_rect)
    return player_score


def reset_game():
    global start_time
    global game_active
    global player_score
    player.sprite.rect.bottom = 300
    player_score = 0
    start_time = int(pygame.time.get_ticks() / 1000)
    game_active = True
    obstacle_group.empty()


def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group.sprites(), False):
        return False
    else:
        return True


# Window
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

# Game logic
game_active = False
player_score = 0

# Groups
player = pygame.sprite.GroupSingle()  # creating GroupSingle for sprite
player.add(Player())  # adding new player sprite

obstacle_group = pygame.sprite.Group()  # creating Group for Multiple sprites

# Text
font = pygame.font.Font('../font/Pixeltype.ttf', 50)
font_large = pygame.font.Font('../font/Pixeltype.ttf', 75)
font_small = pygame.font.Font('../font/Pixeltype.ttf', 25)

# Background
sky_surface = pygame.image.load('../graphics/Sky.png').convert()
ground_surface = pygame.image.load('../graphics/ground.png').convert()


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
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(random.choice(['fly', 'snail', 'snail'])))  # 66% snail chance
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
        player.update()
        player.draw(screen)                             # drawing player GroupSingle onscreen

        # Obstacle
        obstacle_group.update()
        obstacle_group.draw(screen)
        game_active = collision_sprite()

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

# Sprite Class
#
# -- Working without classes may work for a small game, but is
#       unpractical for bigger projects.
# -- Player currently has 4 code snippets - Unpractical to maintain
#
# -- Sprite Class
#   Pygame class that contains a surface and a rectangle
#   Implement a sprite class for player, snail and fly
#
#   Can't use screen.blit for sprite
#   1) Create Sprite.
#   2) Place sprites in Group or GroupSingle.
#   3) Draw/Update all sprites in that group.
#
#   Group - For multiple sprites (flies / snails)
#   GroupSingle - Single sprite (player)
