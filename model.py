class ShipSegment:
	def __init__(self, parent):
		self.hit = False
		self.parent = parent

	def hit(self):
		self.hit = True
		self.parent.updateHits()

	def __str__(self):
		return "X" if hit else " "

class WaterSegment:
	def __init__(self):
		self.miss = False

class Ship:
	def __init__(self, size):
		self.sunk = False
		self.size = size
		self.hits = 0
		# TODO: initialize these segments
		self.segments = []

	def updateHits(self):
		hits = 0
		for segment in self.segments:
			if segment.hit:
				hits += 1

		if hits == size:
			self.sunk = True


class Board:
	def __init__(self, size=10):
		self.cells = []
		for x in range(0, size):
			temp = []
			for y in range(0, 2*size):
				temp.append(None)
			self.cells.append(temp)

class Game:
	def __init__(self, size=10):
		self.board = Board(size)
		self.currentPlayer = 0
		self.turnCount = 0

	def gameStart(self):
		# TODO
