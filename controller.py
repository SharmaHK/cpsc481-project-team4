from model import *
from view import *

class Game:
	def __init__(self, size=10):
		self.humanBoard = Board(size)
		self.aiBoard = Board(size)
		self.humanTurn = True
		self.turnCount = 0
		self.size = size

	def placeShips(self):
		# TODO: have player place ships
		self.humanBoard.addShip(0, 0, 4, "down")
		self.humanBoard.addShip(3, 3, 3, "right")
		self.humanBoard.addShip(1, 4, 2, "left")

		# TODO: generate random ships for the AI

	def gameLoop(self):
		done = False
		while not done:
			event = pygame.event.wait()

			if event.type == pygame.QUIT:
				print("Closing game...")
				self.display.close()
				done = True
				continue
			elif event.type == pygame.MOUSEBUTTONUP:
				# TODO: Handle mouseclicks and check for hits
				# TODO: translate an (x, y) mouseclick into a hit/miss
				x, y = event.pos
				print("Mouseclick at", x, ",", y)

			self.display.updateScreen(self)

	def play(self):
		# TODO: Initialize the display and render the empty grid
		print("Initializing display...")
		# TODO: find a better way to calculate the display size
		self.display = Display(1205, 555)
		self.display.updateScreen(self)

		print("Asking player to place ships...")
		self.placeShips()

		print("Entering main game loop...")
		self.gameLoop()

		# TODO: declare the winner and ask to play again
