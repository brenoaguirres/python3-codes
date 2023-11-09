# Drawing with Rectangles and Colors

import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

font = pygame.font.Font('../font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('../graphics/Sky.png').convert()
ground_surface = pygame.image.load('../graphics/ground.png').convert()

score_surf = font.render('Runner', False, (64, 64, 64)).convert()
score_rect = score_surf.get_rect(center=(400, 50))

snail_surf = pygame.image.load('../graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom=(600, 300))

player_surf = pygame.image.load('../graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEMOTION:
            if player_rect.collidepoint(event.pos):
                print('MOUSE OVER')

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, '#c0e8ec', score_rect)  # make the fill color
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 6, 6)  # drawing with rectangle
            # disp_surface, color, surface, border_width, border_radius
    pygame.draw.line(screen, 'Gold', (0, 0), pygame.mouse.get_pos(), 10)  # draw line to mouse
    pygame.draw.ellipse(screen, 'Brown', pygame.Rect(50, 200, 100, 100))  # creating rect at x, y, w, h
                                                                                # creating ellipse at rect
    screen.blit(score_surf, score_rect)

    snail_rect.right -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800
    screen.blit(snail_surf, snail_rect)

    player_rect.left += 1
    screen.blit(player_surf, player_rect)

    if player_rect.colliderect(snail_rect):
        print('snail collision')

    pygame.display.update()
    clock.tick(60)


# Drawing with rectangles
#   -- pygame.draw
#           draw rectangles, circles, lines, points, ellipses, etc.

# Colors
#   -- RGB or HEXDEC
#       rgb - (0, 0, 0)
#       hex - #rrggbb - 00-FF
