from model import *
from view import *
import random

class Game:
	def __init__(self, size=10):
		self.humanBoard = Board(size)
		self.aiBoard = Board(size)
		self.humanTurn = True
		self.turnCount = 0
		self.size = size

	def placeShips(self):
		# Randomly generate player ships
		remaining = 5
		while remaining > 0:
			x = random.randint(0, self.size-1)
			y = random.randint(0, self.size-1)
			size = random.randint(1, 5)
			slope = random.randint(UP, RIGHT)
			if self.humanBoard.addShip(x, y, size, slope):
				remaining -= 1


		# Randomly generate AI ships
		remaining = 5
		while remaining > 0:
			x = random.randint(0, self.size-1)
			y = random.randint(0, self.size-1)
			size = random.randint(1, 5)
			slope = random.randint(UP, RIGHT)
			if self.aiBoard.addShip(x, y, size, slope):
				remaining -= 1




	def gameLoop(self):
		done = False
		while not done:
			event = pygame.event.wait()

			if event.type == pygame.QUIT:
				print("Closing game...")
				self.display.close()
				done = True
				continue
			if event.type == pygame.MOUSEBUTTONDOWN:
				x, y = event.pos
				cellX, cellY, boardnum = self.display.translateXY(x, y)
				if boardnum == PLAYERBOARD:
					board = self.humanBoard
				else:
					board = self.aiBoard

				board.shoot(cellX, cellY)
			self.display.updateScreen(self)

	def play(self):
		# TODO: Initialize the display and render the empty grid
		print("Initializing display...")
		self.display = Display(self.size)
		self.display.updateScreen(self)

		print("Asking player to place ships...")
		self.placeShips()

		print("Entering main game loop...")
		self.gameLoop()

		# TODO: declare the winner and ask to play again
