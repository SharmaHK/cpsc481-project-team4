class ShipSegment:
	def __init__(self, parent):
		self.hit = False
		self.parent = parent

	def hit(self):
		self.hit = True
		self.parent.updateHits()

	def __str__(self):
		return "X" if self.hit else " "

class WaterSegment:
	def __init__(self):
		self.miss = False

	def __str__(self):
		return "M" if self.miss else " "

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

	def __str__(self):
		if size == 2:
			return "Destroyer"
		elif size == 2:
			return "Cruiser"
		elif size == 4:
			return "Battleship"
		elif size == 5:
			return "Carrier"
		else
			return "Ship"

class Board:
	def __init__(self, size = 10):
		self.cells = []
		for x in range(0, size):
			temp = []
			for y in range(0, size):
				temp.append(None)
			self.cells.append(temp)

	def addShip(self, x, y, size, orientation):
		# make sure ship is on the board
		# make sure the ship does not overlap other ships

class Game:
	def __init__(self, size = 10):
		self.board = Board(size)
		self.currentPlayer = 0
		self.turnCount = 0

	def gameStart(self):
		# TODO
		# add ships
		# start gameloop
