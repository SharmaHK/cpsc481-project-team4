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
		xCarrier = int(input('Enter x coordinate for Carrier: '))
		yCarrier = int(input('Enter y coordinate for Carrier: '))
		zCarrier = input('Enter slope[\'left\',\'right\',\'up\',\'down\'] for Carrier: ')
		self.humanBoard.addShip(xCarrier, yCarrier, 5, zCarrier)

		xBattleship = int(input('Enter x coordinate for Battleship: '))
		yBattleship = int(input('Enter y coordinate for Battleship: '))
		zBattleship = input('Enter slope[\'left\',\'right\',\'up\',\'down\'] for Battleship: ')
		self.humanBoard.addShip(xBattleship, yBattleship, 4, zBattleship)

		xSubmarine = int(input('Enter x coordinate for Submarine: '))
		ySubmarine = int(input('Enter y coordinate for Submarine: '))
		zSubmarine = input('Enter slope[\'left\',\'right\',\'up\',\'down\'] for Cruiser: ')
		self.humanBoard.addShip(xSubmarine, ySubmarine, 3, zSubmarine)

		xCruiser = int(input('Enter x coordinate for Cruiser: '))
		yCruiser = int(input('Enter y coordinate for Cruiser: '))
		zCruiser = input('Enter slope[\'left\',\'right\',\'up\',\'down\'] for Cruiser: ')
		self.humanBoard.addShip(xCruiser, yCruiser, 3, zCruiser)

		xDestroyer = int(input('Enter x coordinate for Destroyer: '))
		yDestroyer = int(input('Enter y coordinate for Destroyer: '))
		zDestroyer = input('Enter slope[\'left\',\'right\',\'up\',\'down\'] forDestroyer: ')
		self.humanBoard.addShip(xDestroyer, yDestroyer, 2, zDestroyer)

		"""
		self.humanBoard.addShip(0, 0, 4, "down") # Battleship
		self.humanBoard.addShip(3, 3, 3, "right")# Cruiser
		self.humanBoard.addShip(1, 4, 2, "left") # Destroyer
		self.humanBoard.addShip(5, 7, 5, "left") # Carrier
		self.humanBoard.addShip(9, 5, 3, "left") # Submarine
		"""

		# TODO: generate random ships for the AI
		"""
		self.aiBoard.addShip(0, 0, 5, "down") # Battleship
		self.aiBoard.addShip(3, 3, 4, "right")# Cruiser
		self.aiBoard.addShip(1, 4, 3, "left") # Destroyer
		self.aiBoard.addShip(5, 7, 6, "left") # Carrier
		self.aiBoard.addShip(9, 5, 4, "left") # Submarine
		"""

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
