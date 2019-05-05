import random
import pygame

class SimpleAI:

	def __init__(self, delay):
		self.delay = delay

	def makeMove(self, game):
		x = random.randint(0, game.size-1)
		y = random.randint(0, game.size-1)
		pygame.time.wait(self.delay)
		return (x, y)
