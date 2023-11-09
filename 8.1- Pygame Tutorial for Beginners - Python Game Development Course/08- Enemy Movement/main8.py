# Enemy Movement

import pygame
from sys import exit


# Classes
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


class Enemy1(pygame.sprite.Sprite):
    def __init__(self, x=32, y=32):
        super().__init__()
        self.image = pygame.image.load('../16- Game Over/images/enemy1.png')
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(midtop=(self.x, self.y))
        self.speed = 1

    def move(self):
        self.y += 64

    def update(self, *args, **kwargs):
        self.rect.y = self.y


class EnemySpawner:
    def __init__(self):
        self.type = None
        self.spawn_x = 45
        self.spawn_y = -64

    def can_spawn(self):
        for enemy in enemies.sprites():
            if enemy.y < 0:
                return False
        return True

    def spawn(self, enemy_type, can_spawn):
        self.type = enemy_type
        if can_spawn:
            if self.type == Enemy1:
                self.spawn_x = 45
                self.spawn_y = -64
                for i in range(0, 12):
                    enemies.add(Enemy1(self.spawn_x, self.spawn_y))
                    self.spawn_x += 64


# Methods
def update_game():
    enemies.update()


def render_game():
    screen.fill((0, 0, 0))
    player.draw(screen)
    enemies.draw(screen)


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
enemies = pygame.sprite.Group()
enemy_spawn = EnemySpawner()
# enemy_spawn.spawn(Enemy1, True)

# In-Game Setup
music.play(loops=-1)
music.set_volume(0.1)

# Custom Events
enemy_movement = pygame.USEREVENT + 1
time_to_move = 2000
pygame.time.set_timer(enemy_movement, time_to_move)

spawn = pygame.USEREVENT + 2
time_to_spawn = time_to_move * 2
pygame.time.set_timer(spawn, time_to_spawn)

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == enemy_movement:
            for enemy in enemies.sprites():
                enemy.move()

        if event.type == spawn:
            enemy_spawn.spawn(Enemy1, enemy_spawn.can_spawn())

    player.sprite.player_input()
    update_game()
    render_game()

    pygame.display.update()
    clock.tick(60)

