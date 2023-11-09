# Text and Displaying Score

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

    def collision(self):
        if pygame.sprite.spritecollide(self, enemies, False):
            global game_active
            game_active = False

    def update(self, *args, **kwargs):
        if (pygame.time.get_ticks() - self.fire_time) / 1000 >= self.fire_cooldown:
            self.can_shoot = True
        self.collision()


class Enemy1(pygame.sprite.Sprite):
    def __init__(self, x=32, y=32):
        super().__init__()
        self.image = pygame.image.load('../16- Game Over/images/enemy1.png').convert_alpha()
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(midtop=(self.x, self.y))
        self.speed = 1
        self.score_value = 50

        # die sfx
        self.sfx = pygame.mixer.Sound('../16- Game Over/audio/expl.wav')
        self.sfx.set_volume(0.08)

    def move(self):
        self.y += 64

    def get_score_value(self):
        return self.score_value

    def play_death_sound(self):
        self.sfx.play()

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
        self.sfx = pygame.mixer.Sound('../16- Game Over/audio/pew.wav')

        self.speed = 15

        # shooting sfx
        self.sfx.set_volume(0.4)
        self.sfx.play()

    def move(self):
        self.y -= self.speed
        self.rect.y = self.y

    def die(self):
        self.kill()

    def collision(self):
        for enemy in enemies.sprites():
            if pygame.sprite.collide_rect(self, enemy):
                enemy.play_death_sound()
                enemy.kill()
                self.die()
                player_score.update_score(enemy.get_score_value())
                return

    def update(self, *args, **kwargs):
        self.move()
        if self.rect.y <= -20:
            self.die()
        self.collision()


class ScoreHandler:
    def __init__(self):
        self.score = 0
        self.x_pos = 10
        self.y_pos = 10

    def update_score(self, score):
        self.score += score

    def display_score(self):
        text = font.render(f"score: {self.score}", True, (255, 255, 255))
        screen.blit(text, (self.x_pos, self.y_pos))


class GameOverState:
    def __init__(self):
        self.menu_player = pygame.transform.smoothscale(player.sprite.image, (200, 200))
        self.menu_player_rect = self.menu_player.get_rect(center=(400, 300))

    def render(self):
        screen.fill((36, 36, 51))
        screen.blit(self.menu_player, self.menu_player_rect)
        text1 = large_font.render('Space Invaders', True, (255, 255, 255))
        text1_rect = text1.get_rect(center=(400, 100))
        if player_score.score > 0:
            text2 = small_font.render(f'You\'ve scored {player_score.score} points!', True,
                                      (255, 255, 255))
        else:
            text2 = small_font.render(f'Press SPACE key to begin.', True,
                                      (255, 255, 255))
        text2_rect = text2.get_rect(center=(400, 500))

        screen.blit(text1, text1_rect)
        screen.blit(text2, text2_rect)


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
    player_score.display_score()


def reset_game():
    player.sprite.rect = player.sprite.image.get_rect(center=(400, 550))
    player_torpedoes.empty()
    enemies.empty()
    player_score.score = 0


# Setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

icon = pygame.image.load('../16- Game Over/images/logo.png').convert_alpha()
pygame.display.set_caption('Space Invaders')
pygame.display.set_icon(icon)

# Resources
music = pygame.mixer.Sound('../16- Game Over/audio/music.mp3')
background = pygame.image.load('../16- Game Over/images/space-bg.jpg').convert()
background = pygame.transform.smoothscale(background, (800, 600))
font = pygame.font.Font('../16- Game Over/fonts/space-xrebron.ttf', 32)
large_font = pygame.font.Font('../16- Game Over/fonts/space-xrebron.ttf', 64)
small_font = pygame.font.Font('../16- Game Over/fonts/space-xrebron.ttf', 16)

# Game Objects
player = pygame.sprite.GroupSingle()
player.add(Player())
enemies = pygame.sprite.Group()
enemy_spawn = EnemySpawner()
player_torpedoes = pygame.sprite.Group()
player_score = ScoreHandler()


# In-Game Setup
music.play(loops=-1)
music.set_volume(0.2)

# Custom Events
enemy_movement = pygame.USEREVENT + 1
time_to_move = 1200
pygame.time.set_timer(enemy_movement, time_to_move)

spawn = pygame.USEREVENT + 2
time_to_spawn = int(time_to_move * 2)
pygame.time.set_timer(spawn, time_to_spawn)

# State Managers
game_active = False
game_over_screen = GameOverState()

# Game Loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == enemy_movement:
                for enemy in enemies.sprites():
                    enemy.move()

            if event.type == spawn:
                enemy_spawn.spawn(Enemy1, enemy_spawn.can_spawn())
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    reset_game()
                    game_active = True

    if game_active:
        player.sprite.player_input()
        update_game()
        render_game()
    else:
        game_over_screen.render()

    pygame.display.update()
    clock.tick(60)

