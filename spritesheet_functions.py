"""
This module is used to pull individual sprites from sprites sheets
"""

import pygame
import constants

class SpriteSheet(object):
	""" Class used to grab images out of a sprite sheet. """

	def __init__(self, file_name):
		# Load the sprite sheet
		self.sprite_sheet = pygame.image.load(file_name).convert()

	def get_image(self, x, y, width, height):
		""" Grab a single image out of a larger SpriteSheet
			pass in the x, y location of the sprite
			and the width and height of the sprite. """

		# Create a new blank image
		image = pygame.Surface([width, height]).convert()
		# Copy the sprite from the Large sheet onto the smaller image
		image.blit(self.sprite_sheet,(0,0),(x,y,width,height))
		# Assuming black works as the transparent colour
		image.set_colorkey(constants.WHITE)
		# Return the image
		return image