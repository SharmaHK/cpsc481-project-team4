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
		return (x, y)
