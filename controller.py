from model import *

class Game:
	def __init__(self, size=10):
		self.humanBoard = Board(size)
		self.aiBoard = Board(size)
		self.humanTurn = True
		self.turnCount = 0

	def play(self):
		# TODO: Initialize the display and render the empty grid
		# TODO: have player place ships
		# TODO: enter the main gameplay loop
		# TODO: declare the winner and ask to play again
		print("Game started")
