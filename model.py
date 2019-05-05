# Declare directions for convenience
UP, DOWN, LEFT, RIGHT = range(4)

class Segment:
	def __init__(self):
		self.beenhit = False

class ShipSegment(Segment):
	def __init__(self, parent):
		super().__init__()
		self.parent = parent
		parent.segments.append(self)

	def hit(self):
		self.beenhit = True
		self.parent.updateHits()

	def __str__(self):
		return "X" if self.beenhit else " "

class WaterSegment(Segment):

	def __str__(self):
		return "M" if self.beenhit else " "

	def hit(self):
		self.beenhit = True

class Ship:
	def __init__(self, size):
		self.sunk = False
		self.size = size
		self.hits = 0
		self.segments = []

	def updateHits(self):
		self.hits = 0
		for segment in self.segments:
			if segment.beenhit:
				self.hits += 1

		if self.hits == self.size:
			self.sunk = True
			print(self, "sunk!")

	def __str__(self):
		if self.size == 2:
			return "Destroyer"
		elif self.size == 3:
			return "Cruiser"
		elif self.size == 3:
			return "Submarine"
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
				temp.append(WaterSegment())
			self.cells.append(temp)
		self.ships = []

	def at(self, x, y):
		if self.valid(x, y):
			return self.cells[x][y]
		return None

	def defeated(self):
		for ship in self.ships:
			if not ship.sunk:
				return False
		return True

	def valid(self, x, y):
		if (0 <= x < self.size) and (0 <= y < self.size):
			return True
		return False

	def shoot(self, x, y):
		target = self.at(x, y)
		if target:
			target.hit()
			return True
		else:
			return False


	def addShip(self, x, y, size, slope):
		"""Attempt to place a given ship at (x, y) with a given slope and size.

		Here slope is one of [UP, DOWN, LEFT, RIGHT], which progress clockwise.
		Returns either True if the placement succeeded, or False if it failed.
		"""

		assert slope in [UP, DOWN, LEFT, RIGHT], "Invalid slope given!"
		assert size > 0, "Can't add ship of size zero!"

		print("Trying to place a ship at", x, y, "with slope", slope, "and size", size)

		locations = []
		locations.append([x, y])

		dx = x
		dy = y

		for i in range(0, size-1):
			if slope == DOWN:
				dy += 1
			elif slope == LEFT:
				dx -= 1
			elif slope == UP:
				dy -= 1
			elif slope == RIGHT:
				dx += 1

			locations.append([dx, dy])

		# Create a ship and create a ShipSegment for each location
		for loc in locations:
			if not self.valid(loc[0], loc[1]) or self.at(loc[0], loc[1]) is ShipSegment:
				return False

		newship = Ship(size)
		for loc in locations:
			self.cells[loc[0]][loc[1]] = ShipSegment(parent=newship)
		self.ships.append(newship)

		return True
