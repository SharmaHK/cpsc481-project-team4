import pygame

from model import *
from controller import *

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Display:
	def __init__(self, width, height):
		pygame.init()
		self.width = width
		self.height = height
		self.margin = 5
		self.screen = pygame.display.set_mode([width, height])
		pygame.display.set_caption("AI Battleship")
		self.clock = pygame.time.Clock()

	def updateScreen(self):
		# Clear the background
		self.screen.fill(BLACK)

		# TODO: Don't draw the AI players ships unless we've hit them
		# TODO: Draw text indicating whoose turn it is and what their scores are
		# TODO: Draw the borders between the segments
		# TODO: Iterate through the model and draw each segment

		# Delay so we run at 60FPS
		self.clock.tick(60)

		# Update the display
		pygame.display.flip()

	def close(self):
		pygame.quit()
