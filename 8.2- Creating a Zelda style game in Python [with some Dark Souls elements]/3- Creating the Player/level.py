# Level class
#
# -- Contains all sprites (player, enemies, map...)
# -- Also deals with their interactions
# -- Needs to be able to manage hundreds of sprites effectively > via groups
#
# -- visible_sprites
# --    group for sprites that will be drawn (only group that draws sprites)
# -- obstacle_sprites
# --    group for sprites that the player can collide with

import pygame
from settings import *
from tile import Tile
from player import Player


class Level:
    def __init__(self):
        # get the display surface
        self.display_surface = pygame.display.get_surface()
        # sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        self.create_map()

        self.player = None

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
                if col == 'p':
                    self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites)

    def run(self):
        # update and draw the game
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
