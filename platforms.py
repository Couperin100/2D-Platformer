"""
Module for managing platforms
"""

import pygame
import constants
from spritesheet_functions import SpriteSheet

# These constants define our platform types
# Name of file
# X location of Sprite
# Y location of sprite
# width of sprite
# Height of sprite

class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """
 
    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        super(Platform,self).__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill(constants.BLACK)
 
        self.rect = self.image.get_rect()