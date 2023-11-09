# Movement Mechanics

import pygame
from sys import exit


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('../16- Game Over/images/ship.png')
        self.x = 400
        self.y = 550
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.speed = 4

    def player_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            if self.rect.left <= 0:
                self.rect.left = 0
            else:
                self.x -= self.speed
                self.rect.x = self.x
        elif keys[pygame.K_d]:
            if self.rect.right >= 800:
                self.rect.right = 800
            else:
                self.x += self.speed
                self.rect.x = self.x


def render_game():
    screen.fill((0, 0, 0))
    player.draw(screen)


# Setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Resources
icon = pygame.image.load('../16- Game Over/images/logo.png').convert_alpha()
pygame.display.set_caption('Space Invaders')
pygame.display.set_icon(icon)

music = pygame.mixer.Sound('../16- Game Over/audio/music.mp3')

# Game Objects
player = pygame.sprite.GroupSingle()
player.add(Player())

# In-Game Setup
music.play(loops=-1)
music.set_volume(0.1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    player.sprite.player_input()

    render_game()
    pygame.display.update()
    clock.tick(60)

