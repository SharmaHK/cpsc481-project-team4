from model import *
from view import *
from ai import *
import random

class Game:
	def __init__(self, size=10):
		self.humanBoard = Board(size)
		self.aiBoard = Board(size)
		self.ai = SimpleAI(100)
		self.humanTurn = True
		self.turnCount = 0
		self.humanScore = 0
		self.aiScore = 0
		self.size = size
		self.winner = None

	def placeShips(self):
		# TODO: have the user decide where to place their ships

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
		self.display.updateScreen(self)
		done = False

		while not done:
			if self.humanTurn:
				playerDone = False
				while not playerDone:
					event = pygame.event.wait()

					if event.type == pygame.QUIT:
						print("Closing game...")
						self.display.close()
						playerDone = True
						continue
					if event.type == pygame.MOUSEBUTTONDOWN:
						x, y = event.pos
						cellX, cellY, boardnum = self.display.translateXY(x, y)

						if boardnum == AIBOARD and not self.aiBoard.at(cellX, cellY).beenhit:
							playerDone = True
							self.aiBoard.shoot(cellX, cellY)
			else:
				x, y = self.ai.makeMove(self)
				self.humanBoard.shoot(x, y)

			# Check for a winner
			if self.humanBoard.defeated():
				self.winner = AIBOARD
				done = True
			elif self.aiBoard.defeated():
				self.winner = PLAYERBOARD
				done = True

			self.turnCount += 1
			self.humanTurn = not self.humanTurn

			self.display.updateScreen(self)

		# TODO: sleep after the game is done

	def play(self):
		print("Initializing display...")
		self.display = Display(self.size)

		self.placeShips()
		self.display.updateScreen(self)

		print("Entering main game loop...")
		self.gameLoop()
