import pygame

from model import *

# Define constants
C_BACKGROUND = (0, 0, 0)
C_PLAYERSHIP = (0, 255, 0)
C_PLAYERHIT = (255, 0, 255)
C_WATER = (0, 0, 255)
C_AISHIP = (255, 0, 0)

MARGIN = 1
CELLSIZE = 50
GUTTER = 80

class Display:
	def __init__(self, width, height):
		pygame.init()
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode([width, height])
		pygame.display.set_caption("AI Battleship")
		self.clock = pygame.time.Clock()

	def updateScreen(self, game):
		# Clear the background
		self.screen.fill(C_BACKGROUND)

		# Draw the player board
		for y in range(0, game.size):
			for x in range(0, game.size):
				dx = (((x + 1) * MARGIN) + (x * CELLSIZE))
				dy = (((y + 1) * MARGIN) + (y * CELLSIZE))

				hcell = game.humanBoard.at(x, y)

				if isinstance(hcell, ShipSegment):
					pygame.draw.rect(self.screen, C_PLAYERSHIP, (dx, dy, CELLSIZE, CELLSIZE))
					if hcell.beenhit:
						pygame.draw.circle(self.screen, C_PLAYERHIT, (dx + 25, dy + 25), CELLSIZE)
				else:
					pygame.draw.rect(self.screen, C_WATER, (dx, dy, CELLSIZE, CELLSIZE))

		# Calculate the x-offset of the AI board
		xoffset = ((game.size * CELLSIZE) + ((game.size + 1) * MARGIN)) + GUTTER

		# Draw the AI board
		for y in range(0, game.size):
			for x in range(0, game.size):
				dx = xoffset + (((x + 1) * MARGIN) + (x * CELLSIZE))
				dy = (((y + 1) * MARGIN) + (y * CELLSIZE))

				acell = game.aiBoard.at(x, y)

				if isinstance(acell, ShipSegment):
					#Change C_AISHIP to C_WATER to hide AI ships
					pygame.draw.rect(self.screen, C_AISHIP, (dx, dy, CELLSIZE, CELLSIZE))
					if acell.beenhit:
						pygame.draw.rect(self.screen, C_AISHIP, (dx, dy, CELLSIZE, CELLSIZE))
				else:
					pygame.draw.rect(self.screen, C_WATER, (dx, dy, CELLSIZE, CELLSIZE))
		# TODO: Don't draw the AI players ships unless we've hit them
		# TODO: Draw text indicating whoose turn it is and what their scores are
		# TODO: Draw the borders between the segments
		# TODO: Iterate through the model and draw each segment

		# Update the display
		pygame.display.flip()

	def close(self):
		pygame.quit()
