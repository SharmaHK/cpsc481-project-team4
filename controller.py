from model import *
from view import *
from ai import *
import random

class Game:
	def __init__(self, size=10):
		self.humanBoard = Board(size)
		self.aiBoard = Board(size)
		self.ai = BetterAI(300)
		self.humanTurn = True
		self.turnCount = 0
		self.size = size
		self.winner = None
		self.debug = False

	def placeShips(self):
		# TODO: have the user decide where to place their ships

		# Randomly generate player ships
		remaining = [5, 4, 3, 3, 2]
		while len(remaining) > 0:
			x = random.randint(0, self.size-1)
			y = random.randint(0, self.size-1)
			slope = random.randint(UP, RIGHT)
			if self.humanBoard.addShip(x, y, remaining[len(remaining) - 1], slope):
				remaining.pop()

		# Randomly generate AI ships
		remaining = [5, 4, 3, 3, 2]
		while len(remaining) > 0:
			x = random.randint(0, self.size-1)
			y = random.randint(0, self.size-1)
			slope = random.randint(UP, RIGHT)
			if self.aiBoard.addShip(x, y, remaining[len(remaining) - 1], slope):
				remaining.pop()

	def gameLoop(self):
		self.display.updateScreen(self)
		done = False

		while not done:
			if self.humanTurn:
				pygame.event.set_allowed([pygame.QUIT, pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN])
				playerDone = False
				while not playerDone:
					event = pygame.event.wait()

					if event.type == pygame.QUIT:
						print("Closing game...")
						self.display.close()
						playerDone = True
						return
					elif event.type == pygame.MOUSEBUTTONDOWN:
						x, y = event.pos
						cellX, cellY, boardnum = self.display.translateXY(x, y)

						if boardnum == AIBOARD and self.aiBoard.at(cellX, cellY) is not None and not self.aiBoard.at(cellX, cellY).beenhit:
							playerDone = True
							self.aiBoard.shoot(cellX, cellY)

							# Disable further events from piling up until the AI is finished making it's move
							pygame.event.set_allowed(None)
							pygame.event.set_allowed(pygame.QUIT)
					elif event.type == pygame.KEYDOWN:
						if event.key == pygame.K_d:
							self.debug = not self.debug
							self.display.updateScreen(self)
			else:
				self.ai.makeMove(self)

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
		pygame.event.set_allowed(pygame.QUIT)
		event = pygame.event.wait()
		return

	def play(self):
		print("Initializing display...")
		self.display = Display(self.size)

		self.placeShips()
		self.display.updateScreen(self)

		print("Entering main game loop...")
		self.gameLoop()
