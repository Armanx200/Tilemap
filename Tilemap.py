# Constants for window width, window height, and tile size
WIN_WIDTH = 640
WIN_HEIGHT = 480
TILESIZE = 32

# Class representing a Tilemap
class Tilemap:
    def __init__(self):
        # Initialize the map with a default character '.'
        self.smooth = [['.'] * ((WIN_WIDTH // TILESIZE) * 2)] * ((WIN_HEIGHT // TILESIZE) * 2)
        self.map = [['.'] * ((WIN_WIDTH // TILESIZE) * 2)] * ((WIN_HEIGHT // TILESIZE) * 2)
        # Define references to neighboring Tilemap instances
        self.right = None
        self.left = None
        self.top = None
        self.bottom = None

    def set_map(self, tile):
        # Set the map based on the provided tile
        x = ((WIN_HEIGHT // TILESIZE) // 2)
        y = ((WIN_WIDTH // TILESIZE) // 2)
        for i in range((WIN_HEIGHT // TILESIZE)):
            self.map[i + x] = self.map[i + x][:y] + tile[i] + self.map[i + x][-y:]

        # Check and create neighboring Tilemap instances if needed
        if self.map != self.smooth:
            if not self.right:
                self.right = Tilemap()
                self.right.left = self
            if not self.left:
                self.left = Tilemap()
                self.left.right = self
            if not self.top:
                self.top = Tilemap()
                self.top.bottom = self
            if not self.bottom:
                self.bottom = Tilemap()
                self.bottom.top = self
        self.fix_map()

    def fix_map(self):
        # Adjust the neighboring maps to ensure continuity
        x = ((WIN_HEIGHT // TILESIZE) // 2)
        y = ((WIN_WIDTH // TILESIZE) // 2)
        height = WIN_HEIGHT // TILESIZE
        width = WIN_WIDTH // TILESIZE
        for i in range(height):
            self.right.map[i + x] = self.map[i + x][width:width + y] + self.right.map[i + x][y:]
            self.left.map[i + x] = self.left.map[i + x][:width + y] + self.map[i + x][y:width]

        for j in range(x + 1):
            self.top.map[j + height + x] = self.top.map[j + height + x][:y] + self.map[x + j][y:width + y] + \
                                           self.top.map[j + height + x][y + width:]
            self.bottom.map[j] = self.bottom.map[j][:y] + self.map[height + j][y:width + y] + self.bottom.map[j][y + width:]

# Create an instance of the Tilemap class
Tile = Tilemap()

# Define the initial tilemap
tilemap = [
    ['B', 'B', 'B' , 'B', 'B', 'B', 'B', '.', '.', '.', '.', '.', '.', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
    ['B', '.', '.' , '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['B', '.', '.' , '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['B', '.', '.' , '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['B', '.', '.' , '.', '.', '.', '.', '.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['.', '.', '.' , 'B', 'B', 'B', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.' , '.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B', '.', '.', '.'],
    ['.', '.', '.' , '.', '.', '.', '.', '.', 'B', '.', 'B', 'B', '.', '.', '.', 'B', 'B', 'B', '.', '.'],
    ['.', '.', '.' , '.', '.', '.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B', '.', '.', '.'],
    ['.', '.', '.' , 'B', 'B', 'B', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['B', '.', '.' , '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['B', '.', '.' , '.', '.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['B', '.', '.' , '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['B', '.', '.' , '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['B', 'B', 'B' , 'B', 'B', 'B', 'B', '.', '.', '.', '.', '.', '.', 'B', 'B', 'B', 'B', 'B', 'B', 'B']
]
# Set the initial tilemap
Tile.set_map(tilemap)

tilemap = [
    ['B', '.', '.' , '.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['B', '.', '.' , '.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['B', '.', '.' , '.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['B', '.', '.' , '.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['B', '.', '.' , '.', '.', '.', '.', '.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['B', '.', '.' , '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['B', '.', '.' , '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['B', '.', '.' , '.', '.', '.', '.', '.', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', '.', '.', '.', 'B'],
    ['B', '.', '.' , '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B', '.', '.', '.', '.', 'B'],
    ['B', '.', '.' , '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B', '.', '.', '.', '.', 'B'],
    ['B', '.', '.' , '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B', '.', '.', '.', '.', 'B'],
    ['B', '.', '.' , '.', '.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['B', '.', '.' , '.', '.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['B', '.', '.' , '.', '.', 'B', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['B', 'B', 'B' , 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']
]
# Set the initial tilemap
Tile.bottom.set_map(tilemap)

tilemap = [
    ['B', 'B', 'B' , 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
    ['B', '.', '.' , '.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['B', '.', '.' , '.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['B', '.', '.' , '.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['B', '.', '.' , '.', '.', '.', '.', '.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['B', '.', '.' , '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['B', '.', '.' , '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['B', '.', '.' , '.', '.', '.', '.', '.', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', '.', '.', '.', 'B'],
    ['B', '.', '.' , '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B', '.', '.', '.', '.', 'B'],
    ['B', '.', '.' , '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B', '.', '.', '.', '.', 'B'],
    ['B', '.', '.' , '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B', '.', '.', '.', '.', 'B'],
    ['B', '.', '.' , '.', '.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['B', '.', '.' , '.', '.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['B', '.', '.' , '.', '.', 'B', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['B', '.', '.' , '.', '.', '.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B']
]
# Set the initial tilemap
Tile.top.set_map(tilemap)

tilemap = [
    ['.', '.', '.' , '.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['.', '.', '.' , '.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['.', '.', '.' , '.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['.', '.', '.' , '.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['.', '.', '.' , '.', '.', '.', '.', '.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['.', '.', '.' , '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['.', '.', '.' , '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['.', '.', '.' , '.', '.', '.', '.', '.', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', '.', '.', '.', 'B'],
    ['.', '.', '.' , '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B', '.', '.', '.', '.', 'B'],
    ['.', '.', '.' , '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B', '.', '.', '.', '.', 'B'],
    ['.', '.', '.' , '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B', '.', '.', '.', '.', 'B'],
    ['.', '.', '.' , '.', '.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['.', '.', '.' , '.', '.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['.', '.', '.' , '.', '.', 'B', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['.', '.', '.' , '.', '.', '.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B']
]
# Set the initial tilemap
Tile.right.set_map(tilemap)

tilemap = [
    ['B', '.', '.' , '.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['B', '.', '.' , '.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['B', '.', '.' , '.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['B', '.', '.' , '.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['B', '.', '.' , '.', '.', '.', '.', '.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['B', '.', '.' , '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['B', '.', '.' , '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['B', '.', '.' , '.', '.', '.', '.', '.', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', '.', '.', '.', '.'],
    ['B', '.', '.' , '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B', '.', '.', '.', '.', '.'],
    ['B', '.', '.' , '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B', '.', '.', '.', '.', '.'],
    ['B', '.', '.' , '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B', '.', '.', '.', '.', '.'],
    ['B', '.', '.' , '.', '.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['B', '.', '.' , '.', '.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['B', '.', '.' , '.', '.', 'B', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['B', '.', '.' , '.', '.', '.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
]
# Set the initial tilemap
Tile.left.set_map(tilemap)

# Print the resulting map
for i in Tile.map:
    for j in i:
        print(j, end='')
    print()