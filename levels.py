import pygame
import constants
import platforms

class Level(object):
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """
 
    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = None
        self.enemy_list = None
         
        # Background image
        self.background = None
        self.foreground = None
        #how far this world has been scrolled left/right
        self.world_shift = 0
        self.level_limit = -1000
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player
 
    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()
 
    def draw(self, screen):
        """ Draw everything on this level. """
 
        # Draw the background
        screen.fill(constants.BLUE)
        screen.blit(self.background,(self.world_shift // 3,0))
        screen.blit(self.midground,(self.world_shift * 1,570))
        screen.blit(self.foreground,(self.world_shift * 4,650))
 
        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):
        "When the player moves left/right and we need to scroll everything"

        #keep track of the shift amount
        self.world_shift += shift_x

        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
 
 
# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """
 
    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("graphics/planet_background.jpg").convert()
        self.midground = pygame.image.load("graphics/planet_mid_background1.png").convert_alpha()
        self.foreground = pygame.image.load("graphics/planet_foreground1.png").convert_alpha()

        self.background.scroll(-110,-110)
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1000
 
        # Array with width, height, x and y of platform
        level = [[210, 40, 500, 470],
                 [210, 40, 200, 400],
                 [210, 40, 600, 300],
                 [210, 40, 900, 300],
                 [210, 40, 1200, 400],
                 [80, 40, 1000, 470]
                 ]
 
        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
