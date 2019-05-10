import pygame

from model import *

# Define constants
C_BACKGROUND = (0, 0, 0)
C_PLAYERSHIP = (0, 255, 0)
C_WATER = (0, 0, 255)
C_HIT = (255, 0, 0)
C_MISS = (255, 255, 255)
C_SUNK = (128, 128, 128)

MARGIN = 5
GUTTER = 150
CELLSIZE = 50
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

	def drawShip(self, ship):

		width = 0
		height = 0

		length = (CELLSIZE * ship.size) + (MARGIN * (ship.size - 1))

		if ship.slope == UP:
			x, y = self.cellXY(ship.x, ship.y - (ship.size - 1), PLAYERBOARD)
			width = CELLSIZE
			height = length

		elif ship.slope == DOWN:
			x, y = self.cellXY(ship.x, ship.y, PLAYERBOARD)
			width = CELLSIZE
			height = length

		elif ship.slope == LEFT:
			x, y = self.cellXY(ship.x - (ship.size - 1), ship.y, PLAYERBOARD)
			width = length
			height = CELLSIZE

		elif ship.slope == RIGHT:
			x, y = self.cellXY(ship.x, ship.y, PLAYERBOARD)
			width = length
			height = CELLSIZE


		if ship.sunk:
			color = C_SUNK
		else:
			color = C_PLAYERSHIP

		pygame.draw.rect(self.screen, color, (x, y, width, height))

	def updateScreen(self, game):
		# Clear the background
		self.screen.fill(C_BACKGROUND)

		# Draw the ships
		if not game.debug:
			for ship in game.humanBoard.ships:
				self.drawShip(ship)

		# Draw the water, misses or debug states
		for y in range(0, game.size):
			for x in range(0, game.size):

				dx, dy = self.cellXY(x, y, PLAYERBOARD)

				hcell = game.humanBoard.at(x, y)

				if not game.debug:
					if isinstance(hcell, WaterSegment):
						pygame.draw.rect(self.screen, C_WATER, (dx, dy, CELLSIZE, CELLSIZE))
						if hcell.beenhit:
							pygame.draw.circle(self.screen, C_MISS, (dx + int(CELLSIZE/2), dy + int(CELLSIZE/2)), HITRADIUS)

					elif isinstance(hcell, ShipSegment):
						if hcell.beenhit:
							pygame.draw.circle(self.screen, C_HIT, (dx + int(CELLSIZE/2), dy + int(CELLSIZE/2)), HITRADIUS)

				elif game.ai.state:
					prob = game.ai.state[x][y]
					a = pygame.Vector3((0, 0, 0))
					b = pygame.Vector3((255, 255, 255))

					t = max(min((prob - 0.2), 1), 0)

					color = a.lerp(b, t)
					pygame.draw.rect(self.screen, (color.x, color.y, color.z), (dx, dy, CELLSIZE, CELLSIZE))

		# Draw the AI board
		for y in range(0, game.size):
			for x in range(0, game.size):

				dx, dy = self.cellXY(x, y, AIBOARD)

				acell = game.aiBoard.at(x, y)

				pygame.draw.rect(self.screen, C_WATER, (dx, dy, CELLSIZE, CELLSIZE))

				if acell.beenhit:
					if isinstance(acell, ShipSegment):
						pygame.draw.circle(self.screen, C_HIT, (dx + int(CELLSIZE/2), dy + int(CELLSIZE/2)), HITRADIUS)
					else:
						pygame.draw.circle(self.screen, C_MISS, (dx + int(CELLSIZE/2), dy + int(CELLSIZE/2)), HITRADIUS)

		# Draw the text elements in the middle
		textCenter = self.rightboardstart - int(GUTTER/2)

		if game.humanTurn:
			turnText = self.font.render("Your turn", True, (255, 255, 255))
		else:
			turnText = self.font.render("AI thinking", True, (255, 255, 255))
		w = turnText.get_width()
		self.screen.blit(turnText, (textCenter - int(w/2), 30))

		scoreText = self.font.render("Score:", True, (255, 255, 255))
		w = scoreText.get_width()
		self.screen.blit(scoreText, (textCenter - int(w/2), 100))

		score = self.font.render(str(game.aiBoard.hits) +" - " + str(game.humanBoard.hits), True, (255, 255, 255))
		w = score.get_width()
		self.screen.blit(score, (textCenter - int(w/2), 130))

		winner = None
		if game.winner == PLAYERBOARD:
			winner = "Player"
		elif game.winner == AIBOARD:
			winner = "AI"

		if winner:
			winText = self.font.render(str(winner) + " wins!", True, (255, 255, 255))
			w = winText.get_width()
			self.screen.blit(winText, (textCenter - int(w/2), 180))

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
