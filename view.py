import pygame

from model import *

# Define constants
C_BACKGROUND = (0, 0, 0)
C_PLAYERSHIP = (0, 255, 0)
C_WATER = (0, 0, 255)
C_AISHIP = (255, 0, 0)
C_PLAYERHIT = C_AISHIP
C_AIHIT = C_PLAYERSHIP
C_SUNK = (128, 128, 128)

MARGIN = 5
GUTTER = 150
CELLSIZE = 25
HITRADIUS = int(CELLSIZE/3)

PLAYERBOARD, AIBOARD = range(2)

class Display:
	def __init__(self, size):
		pygame.init()

		self.totalmargins = MARGIN * (size + 1)
		self.boardsize = size * CELLSIZE
		self.size = size

		self.rightboardstart = self.boardsize + self.totalmargins + GUTTER

		self.width = (self.boardsize * 2) + GUTTER + (2 * self.totalmargins)
		self.height = self.boardsize + self.totalmargins

		self.screen = pygame.display.set_mode([self.width, self.height])

		pygame.display.set_caption("AI Battleship")
		self.clock = pygame.time.Clock()
		self.font = pygame.font.Font(pygame.font.get_default_font(), 24)

	def cellXY(self, x, y, board):
		"""Returns the x and y offsets of the desired cell on the desired board"""
		u = 0
		v = (MARGIN * (y + 1)) + (CELLSIZE * y)
		if board == PLAYERBOARD:
			u = (MARGIN * (x + 1)) + (CELLSIZE * x)
		else:
			u = self.rightboardstart + (MARGIN * (x + 1)) + (CELLSIZE * x)

		return (u, v)

	def updateScreen(self, game):
		# Clear the background
		self.screen.fill(C_BACKGROUND)

		# Draw the player board
		for y in range(0, game.size):
			for x in range(0, game.size):

				dx, dy = self.cellXY(x, y, PLAYERBOARD)

				hcell = game.humanBoard.at(x, y)

				if isinstance(hcell, ShipSegment):
					if hcell.parent.sunk:
						color = C_SUNK
					else:
						color = C_PLAYERSHIP
					pygame.draw.rect(self.screen, color, (dx, dy, CELLSIZE, CELLSIZE))

					if hcell.beenhit:
						pygame.draw.circle(self.screen, C_PLAYERHIT, (dx + int(CELLSIZE/2), dy + int(CELLSIZE/2)), HITRADIUS)
				else:
					pygame.draw.rect(self.screen, C_WATER, (dx, dy, CELLSIZE, CELLSIZE))

		# Draw the AI board
		for y in range(0, game.size):
			for x in range(0, game.size):

				dx, dy = self.cellXY(x, y, AIBOARD)

				acell = game.aiBoard.at(x, y)

				if isinstance(acell, ShipSegment) and acell.beenhit:
					if acell.parent.sunk:
						color = C_SUNK
					else:
						color = C_AISHIP
					pygame.draw.rect(self.screen, color, (dx, dy, CELLSIZE, CELLSIZE))
					pygame.draw.circle(self.screen, C_AIHIT, (dx + int(CELLSIZE/2), dy + int(CELLSIZE/2)), HITRADIUS)
				else:
					pygame.draw.rect(self.screen, C_WATER, (dx, dy, CELLSIZE, CELLSIZE))

		# TODO: Draw text indicating whoose turn it is and what their scores are
		text = self.font.render("Hello world", True, (255, 255, 255))
		self.screen.blit(text, (self.rightboardstart - GUTTER, 100))

		# Update the display
		pygame.display.flip()

	def translateXY(self, x, y):
		"""Given an (X, Y) coordinate in the screen, return the coordinates and the board that was clicked on, or None if no board"""

		board = None
		u = 0
		v = 0

		if 0 <= x <= (self.boardsize + self.totalmargins):
			u = x // (CELLSIZE + MARGIN)
			v = y // (CELLSIZE + MARGIN)
			board = PLAYERBOARD
		elif self.rightboardstart <= x <= self.width:
			u = (x - self.rightboardstart) // (CELLSIZE + MARGIN)
			v = y // (CELLSIZE + MARGIN)
			board = AIBOARD

		return (int(u), int(v), board)

	def translateBoard(self, board):
		"""Translate the board enum into a string for display"""
		if board == PLAYERBOARD:
			return "player"
		elif board == AIBOARD:
			return "ai"
		else:
			return None


	def close(self):
		pygame.quit()
