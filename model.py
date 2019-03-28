class ShipSegment:
	def __init__(self, parent):
		self.beenhit = False
		self.parent = parent

	def hit(self):
		self.beenhit = True
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

		if hits == self.size:
			self.sunk = True

	def __str__(self):
		if self.size == 2:
			return "Destroyer"
		elif self.size == 2:
			return "Cruiser"
		elif self.size == 4:
			return "Battleship"
		elif self.size == 5:
			return "Carrier"
		else:
			return "Ship"

class Board:
	def __init__(self, size = 10):
		self.cells = []
		self.size = size
		for x in range(0, size):
			temp = []
			for y in range(0, size):
				temp.append(None)
			self.cells.append(temp)
		self.ships = []

	def at(self, x, y):
		if (0 <= x < self.size) and (0 <= y < self.size):
			return self.cells[x][y]
		return None

	def valid(self, x, y):
		if (0 <= x < self.size) and (0 <= y < self.size):
			return True
		return False

	def addShip(self, x, y, size, slope):
		"""Attempt to place a given ship at (x, y) with a given slope and size.

		Here slope is one of ["down", "left", "up", "right"], which progress clockwise.
		Returns either True if the placement succeeded, or False if it failed.
		"""

		assert slope in ["down", "left", "up", "right"], "Invalid slope given!"
		assert self.valid(x, y), "Invalid location given!"

		locations = []
		locations.append([x, y])

		dx = x
		dy = y

		for i in range(1, size-1):
			if slope == "down":
				dy += 1
			elif slope == "left":
				dx -= 1
			elif slope == "up":
				dy -= 1
			elif slope == "right":
				dx += 1

			if self.valid(dx, dy):
				locations.append([dx, dy])
			else:
				# If we can't place a ship at that location, return false
				return False

		# Create a ship and create a ShipSegment for each location
		newship = Ship(size)
		for loc in locations:
			self.cells[loc[0]][loc[1]] = ShipSegment(parent=newship)

		return True

	# TODO: add a addRandomShips function to populate the AI board


