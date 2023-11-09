# Background Image

import pygame
from sys import exit


# Classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('../16- Game Over/images/ship.png').convert_alpha()
        self.x = 400
        self.y = 550
        self.rect = self.image.get_rect(center=(self.x, self.y))

        # movement
        self.speed = 4

        # shooting
        self.fire_cooldown = 0.3
        self.fire_time = 0
        self.can_shoot = True

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
        if keys[pygame.K_SPACE] and self.can_shoot:
            player_torpedoes.add(Torpedo(self.rect))
            self.can_shoot = False
            self.fire_time = pygame.time.get_ticks()

    def update(self, *args, **kwargs):
        if (pygame.time.get_ticks() - self.fire_time) / 1000 >= self.fire_cooldown:
            self.can_shoot = True


class Enemy1(pygame.sprite.Sprite):
    def __init__(self, x=32, y=32):
        super().__init__()
        self.image = pygame.image.load('../16- Game Over/images/enemy1.png').convert_alpha()
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


class Torpedo(pygame.sprite.Sprite):
    def __init__(self, player_rect):
        super().__init__()
        self.image = pygame.image.load('../16- Game Over/images/missile.png').convert_alpha()
        self.x = player_rect.centerx
        self.y = player_rect.centery
        self.rect = self.image.get_rect(center=(self.x, self.y))

        self.speed = 15

    def move(self):
        self.y -= self.speed
        self.rect.y = self.y

    def die(self):
        self.kill()

    def update(self, *args, **kwargs):
        self.move()
        if self.rect.y <= -20:
            self.die()


# Methods
def update_game():
    player_torpedoes.update()
    player.update()
    enemies.update()


def render_game():
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    player_torpedoes.draw(screen)
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
background = pygame.image.load('../16- Game Over/images/space-bg.jpg').convert()
background = pygame.transform.smoothscale(background, (800, 600))

# Game Objects
player = pygame.sprite.GroupSingle()
player.add(Player())
enemies = pygame.sprite.Group()
enemy_spawn = EnemySpawner()
player_torpedoes = pygame.sprite.Group()

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

