import random
import pygame

class SimpleAI:

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

# TODO: Implement a more advanced AI

class BetterAI:

	def __init__(self, delay):
		self.delay = delay
		self.state = None
		self.size = None

	def bestGuess(self):
		# Choose a random location on the grid
		x = random.randint(0, self.size-1)
		y = random.randint(0, self.size-1)

		# Look for a better guess
		# TODO: make this pick randomly if there are multiple best guesses
		for u in range(0, self.size):
			for v in range(0, self.size):
				if self.state[u][v] > self.state[x][y]:
					x = u
					y = v
		return (x, y)

	def updateSurrounding(self, x, y, delta):
		locations = []
		locations.append([x+1, y+1])
		locations.append([x+1, y-1])
		locations.append([x-1, y+1])
		locations.append([x-1, y-1])

		for loc in locations:
			u = loc[0]
			v = loc[1]
			if (0 <= u < self.size) and (0 <= v < self.size):
				self.state[u][v] += delta

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

		if game.humanBoard.shoot(x, y):
			self.state[x][y] = -100
			self.updateSurrounding(x, y, 50)
		else:
			self.state[x][y] = -100
			self.updateSurrounding(x, y, -1)
