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
		"""
		self.aiBoard.addShip(0, 0, 4, "down") # Battleship
		self.aiBoard.addShip(3, 3, 3, "right")# Cruiser
		self.aiBoard.addShip(1, 4, 2, "left") # Destroyer
		self.aiBoard.addShip(5, 7, 5, "left") # Carrier
		self.aiBoard.addShip(9, 5, 3, "left") # Submarine
		"""
		randPlayerBoard = random.randint(0,9)
		randAiBoard = random.randint(0,9)

		#Generating Player Board
		if randPlayerBoard is 0:
			self.humanBoard.addShip(0, 0, 4, "down") # Battleship
			self.humanBoard.addShip(3, 3, 3, "right")# Cruiser
			self.humanBoard.addShip(1, 4, 2, "left") # Destroyer
			self.humanBoard.addShip(5, 7, 5, "left") # Carrier
			self.humanBoard.addShip(9, 5, 3, "left") # Submarine
		elif randPlayerBoard is 1:
			self.humanBoard.addShip(1, 9, 4, "right")
			self.humanBoard.addShip(1, 1, 3, "right")
			self.humanBoard.addShip(9, 9, 2, "up")
			self.humanBoard.addShip(1, 7, 5, "right")
			self.humanBoard.addShip(7, 4, 3, "up")
		elif randPlayerBoard is 2:
			self.humanBoard.addShip(6, 8, 4, "up")
			self.humanBoard.addShip(9, 2, 3, "down")
			self.humanBoard.addShip(8, 9, 2, "left")
			self.humanBoard.addShip(1, 2, 5, "down")
			self.humanBoard.addShip(1, 8, 3, "right")
		elif randPlayerBoard is 3:
			self.humanBoard.addShip(5, 4, 4, "right")
			self.humanBoard.addShip(1, 3, 3, "right")
			self.humanBoard.addShip(8, 8, 2, "up")
			self.humanBoard.addShip(1, 8, 5, "right")
			self.humanBoard.addShip(6, 6, 3, "left")
		elif randPlayerBoard is 4:
			self.humanBoard.addShip(8, 8, 4, "up")
			self.humanBoard.addShip(3, 3, 3, "down")
			self.humanBoard.addShip(1, 8, 2, "left")
			self.humanBoard.addShip(1, 1, 5, "down")
			self.humanBoard.addShip(9, 3, 3, "left")
		elif randPlayerBoard is 5:
			self.humanBoard.addShip(8, 1, 4, "down")
			self.humanBoard.addShip(8, 8, 3, "left")
			self.humanBoard.addShip(3, 4, 2, "left")
			self.humanBoard.addShip(1, 2, 5, "right")
			self.humanBoard.addShip(2, 9, 3, "up")
		elif randPlayerBoard is 6:
			self.humanBoard.addShip(1, 8, 4, "right")
			self.humanBoard.addShip(8, 8, 3, "left")
			self.humanBoard.addShip(1, 2, 2, "right")
			self.humanBoard.addShip(6, 5, 5, "up")
			self.humanBoard.addShip(1, 6, 3, "right")
		elif randPlayerBoard is 7:
			self.humanBoard.addShip(9, 3, 4, "down")
			self.humanBoard.addShip(1, 8, 3, "up")
			self.humanBoard.addShip(3, 4, 2, "up")
			self.humanBoard.addShip(2, 1, 5, "right")
			self.humanBoard.addShip(9, 0, 3, "left")
		elif randPlayerBoard is 8:
			self.humanBoard.addShip(1, 8, 4, "right")
			self.humanBoard.addShip(5, 4, 3, "right")
			self.humanBoard.addShip(1, 1, 2, "right")
			self.humanBoard.addShip(1, 6, 5, "right")
			self.humanBoard.addShip(6, 9, 3, "right")
		elif randPlayerBoard is 9:
			self.humanBoard.addShip(8, 8, 4, "up")
			self.humanBoard.addShip(1, 1, 3, "right")
			self.humanBoard.addShip(4, 5, 2, "right")
			self.humanBoard.addShip(9, 0, 5, "left")
			self.humanBoard.addShip(2, 5, 3, "up")

		#Generating AI Board
		if randAiBoard is 0:
			self.aiBoard.addShip(0, 0, 4, "down") # Battleship
			self.aiBoard.addShip(3, 3, 3, "right")# Cruiser
			self.aiBoard.addShip(1, 4, 2, "left") # Destroyer
			self.aiBoard.addShip(5, 7, 5, "left") # Carrier
			self.aiBoard.addShip(9, 5, 3, "left") # Submarine
		elif randAiBoard is 1:
			self.aiBoard.addShip(1, 9, 4, "right")
			self.aiBoard.addShip(1, 1, 3, "right")
			self.aiBoard.addShip(9, 9, 2, "up")
			self.aiBoard.addShip(1, 7, 5, "right")
			self.aiBoard.addShip(7, 4, 3, "up")
		elif randAiBoard is 2:
			self.aiBoard.addShip(6, 8, 4, "up")
			self.aiBoard.addShip(9, 2, 3, "down")
			self.aiBoard.addShip(8, 9, 2, "left")
			self.aiBoard.addShip(1, 2, 5, "down")
			self.aiBoard.addShip(1, 8, 3, "right")
		elif randAiBoard is 3:
			self.aiBoard.addShip(5, 4, 4, "right")
			self.aiBoard.addShip(1, 3, 3, "right")
			self.aiBoard.addShip(8, 8, 2, "up")
			self.aiBoard.addShip(1, 8, 5, "right")
			self.aiBoard.addShip(6, 6, 3, "left")
		elif randAiBoard is 4:
			self.aiBoard.addShip(8, 8, 4, "up")
			self.aiBoard.addShip(3, 3, 3, "down")
			self.aiBoard.addShip(1, 8, 2, "left")
			self.aiBoard.addShip(1, 1, 5, "down")
			self.aiBoard.addShip(9, 3, 3, "left")
		elif randAiBoard is 5:
			self.aiBoard.addShip(8, 1, 4, "down")
			self.aiBoard.addShip(8, 8, 3, "left")
			self.aiBoard.addShip(3, 4, 2, "left")
			self.aiBoard.addShip(1, 2, 5, "right")
			self.aiBoard.addShip(2, 9, 3, "up")
		elif randAiBoard is 6:
			self.aiBoard.addShip(1, 8, 4, "right")
			self.aiBoard.addShip(8, 8, 3, "left")
			self.aiBoard.addShip(1, 2, 2, "right")
			self.aiBoard.addShip(6, 5, 5, "up")
			self.aiBoard.addShip(1, 6, 3, "right")
		elif randAiBoard is 7:
			self.aiBoard.addShip(9, 3, 4, "down")
			self.aiBoard.addShip(1, 8, 3, "up")
			self.aiBoard.addShip(3, 4, 2, "up")
			self.aiBoard.addShip(2, 1, 5, "right")
			self.aiBoard.addShip(9, 0, 3, "left")
		elif randAiBoard is 8:
			self.aiBoard.addShip(1, 8, 4, "right")
			self.aiBoard.addShip(5, 4, 3, "right")
			self.aiBoard.addShip(1, 1, 2, "right")
			self.aiBoard.addShip(1, 6, 5, "right")
			self.aiBoard.addShip(6, 9, 3, "right")
		elif randAiBoard is 9:
			self.aiBoard.addShip(8, 8, 4, "up")
			self.aiBoard.addShip(1, 1, 3, "right")
			self.aiBoard.addShip(4, 5, 2, "right")
			self.aiBoard.addShip(9, 0, 5, "left")
			self.aiBoard.addShip(2, 5, 3, "up")




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
				cellX, cellY, board = self.display.translateXY(x, y)
				print("Mouseclick at", cellX, ",", cellY, "on board", self.display.translateBoard(board))
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
