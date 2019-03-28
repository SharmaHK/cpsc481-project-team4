from model import *
from view import *

class Game:
	def __init__(self, size=10):
		self.humanBoard = Board(size)
		self.aiBoard = Board(size)
		self.humanTurn = True
		self.turnCount = 0

	def placeShips(self):
		# TODO: have player place ships

	def gameLoop(self):
		done = False
		while not done:
			# TODO: Handle mouseclicks and check for hits
			print("Event happened!")

	def play(self):
		# TODO: Initialize the display and render the empty grid
		print("Initializing display...")
		self.display = Display(1000, 500)
		self.display.updateBoard(humanBoard, aiBoard)

		print("Asking player to place ships...")
		self.placeShips()

		print("Entering main game loop...")
		self.gameLoop()

		# TODO: declare the winner and ask to play again
