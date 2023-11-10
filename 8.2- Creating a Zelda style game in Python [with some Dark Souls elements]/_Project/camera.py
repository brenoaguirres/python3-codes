# Camera
#
# -- Both a camera and overlap can be achieved by customizing a group
# -- The main purpose of a group is:
#       1) Store and draw sprites
#       2) call the update method
# -- But you can add methods or change how groups work (we will draw a custom draw method for example)
#
# -- What a sprite group does:
#   group.sprites()
#   for sprite in sprites():
#       sprite.update()
#
#   draw(surface)
#   for sprite in sprites():
#       surface.blit(sprite.image, sprite.rect)
#
# -- Lets change the visible_sprites group to a custom-made group
# -- this group will have a custom_draw
# -- for sprite in sprites():
#       surface.blit(sprite.image, sprite.rect+offset)
#           offset comes from player position

