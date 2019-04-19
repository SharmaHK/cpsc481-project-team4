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
		# TODO: have player place ships
		"""
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

		# TODO: generate random ships for the AI
		randIntX = random.randint(0,9)
		randIntY = random.randint(0,9)
		randShip = random.randint(2,5)
		randIntSlope = random.randint(0,3)
		randSlope = ""
		if randIntSlope is 0:
			randSlope = "right"
		elif randIntSlope is 1:
			randSlope = "down"
		elif randIntSlope is 2:
			randSlope = "left"
		elif randIntSlope is 3:
			randSlope = "up"
		self.aiBoard.addShip(randIntX, randIntY, 4, randSlope) # Battleship

		randIntX = random.randint(0,9)
		randIntY = random.randint(0,9)
		randShip = random.randint(2,5)
		randIntSlope = random.randint(0,3)
		if randIntSlope is 0:
			randSlope = "right"
		elif randIntSlope is 1:
			randSlope = "down"
		elif randIntSlope is 2:
			randSlope = "left"
		elif randIntSlope is 3:
			randSlope = "up"
		self.aiBoard.addShip(randIntX, randIntY, 3, randSlope)# Cruiser

		randIntX = random.randint(0,9)
		randIntY = random.randint(0,9)
		randShip = random.randint(2,5)
		randIntSlope = random.randint(0,3)
		if randIntSlope is 0:
			randSlope = "right"
		elif randIntSlope is 1:
			randSlope = "down"
		elif randIntSlope is 2:
			randSlope = "left"
		elif randIntSlope is 3:
			randSlope = "up"
		self.aiBoard.addShip(randIntX, randIntY, 2, randSlope) # Destroyer

		randIntX = random.randint(0,9)
		randIntY = random.randint(0,9)
		randShip = random.randint(2,5)
		randIntSlope = random.randint(0,3)
		if randIntSlope is 0:
			randSlope = "right"
		elif randIntSlope is 1:
			randSlope = "down"
		elif randIntSlope is 2:
			randSlope = "left"
		elif randIntSlope is 3:
			randSlope = "up"
		self.aiBoard.addShip(randIntX, randIntY, 5, randSlope) # Carrier

		randIntX = random.randint(0,9)
		randIntY = random.randint(0,9)
		randShip = random.randint(2,5)
		randIntSlope = random.randint(0,3)
		if randIntSlope is 0:
			randSlope = "right"
		elif randIntSlope is 1:
			randSlope = "down"
		elif randIntSlope is 2:
			randSlope = "left"
		elif randIntSlope is 3:
			randSlope = "up"
		self.aiBoard.addShip(randIntX, randIntY, 3, randSlope) # Submarine

		"""
		self.aiBoard.addShip(0, 0, 4, "down") # Battleship
		self.aiBoard.addShip(3, 3, 3, "right")# Cruiser
		self.aiBoard.addShip(1, 4, 2, "left") # Destroyer
		self.aiBoard.addShip(5, 7, 5, "left") # Carrier
		self.aiBoard.addShip(9, 5, 3, "left") # Submarine
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
			if event.type == pygame.MOUSEBUTTONDOWN:
				# TODO: Handle mouseclicks and check for hits
				# TODO: translate an (x, y) mouseclick into a hit/miss
				x, y = event.pos
				aiX = (x//50)-12
				aiY = y//50
				print("Mouseclick at", aiX, ",", aiY)
			self.display.updateScreen(self)

	def play(self):
		# TODO: Initialize the display and render the empty grid
		print("Initializing display...")
		# TODO: find a better way to calculate the display size
		self.display = Display(1100, 510)
		self.display.updateScreen(self)

		print("Asking player to place ships...")
		self.placeShips()

		print("Entering main game loop...")
		self.gameLoop()

		# TODO: declare the winner and ask to play again
