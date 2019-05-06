import random
import pygame
from model import *

class SimpleAI:
	""" Makes random guesses and hopes for the best"""

	def __init__(self, delay):
		self.delay = delay

	def makeMove(self, game):
		done = False
		while not done:
			x = random.randint(0, game.size-1)
			y = random.randint(0, game.size-1)
			if not game.humanBoard.at(x, y).beenhit:
				done = True

		pygame.time.wait(self.delay)
		game.humanBoard.shoot(x, y)


class BetterAI:
	"""Uses the hueristic that if a cell is a hit it's neighbors are also likely to be ships"""

	def __init__(self, delay):
		self.delay = delay
		self.state = None
		self.size = None

	def bestGuess(self):

		x = random.randint(0, self.size-1)
		y = random.randint(0, self.size-1)
		best = self.state[x][y]
		locations = []

		# Update best and the list of equal valued locations
		for u in range(0, self.size):
			for v in range(0, self.size):
				if self.state[u][v] > best:
					locations = [[u, v]]
					best = self.state[u][v]
				elif self.state[u][v] == best:
					locations.append([u, v])

		# Randomly choose from the locations with equal probablility
		chosen = locations[random.randint(0, len(locations)-1)]

		x = chosen[0]
		y = chosen[1]

		return (x, y)

	def updateSurrounding(self, x, y, delta):
		"""Updates the probabilites surrounding a cell by delta"""

		close = []
		close.append([x+1, y])
		close.append([x-1, y])
		close.append([x, y+1])
		close.append([x, y-1])

		far = []
		far.append([x+2, y])
		far.append([x-2, y])
		far.append([x, y+2])
		far.append([x, y-2])

		for loc in close:
			u = loc[0]
			v = loc[1]
			if (0 <= u < self.size) and (0 <= v < self.size):
				self.state[u][v] += delta

		for loc in far:
			u = loc[0]
			v = loc[1]
			if (0 <= u < self.size) and (0 <= v < self.size):
				self.state[u][v] += (delta/2)

	def makeMove(self, game):

		# If the AI state is uninitalized, intialize it
		if self.state is None:
			self.size = game.size
			self.state = []
			for u in range(0, game.size):
				self.state.append([])
				for v in range(0, game.size):
					self.state[u].append(0)

		# Find our best guess
		x, y = self.bestGuess()

		# Wait a bit to increase player anticipation
		pygame.time.wait(self.delay)

		# Shoot the cell
		game.humanBoard.shoot(x, y)

		# Make sure we don't pick that cell again
		self.state[x][y] = -1000

		# Check if we hit a ship and update our state
		if isinstance(game.humanBoard.at(x, y), ShipSegment):
			self.updateSurrounding(x, y, 50)
		else:
			self.updateSurrounding(x, y, -10)
