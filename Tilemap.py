# Constants for window width, window height, and tile size
WIN_WIDTH = 640
WIN_HEIGHT = 480
TILESIZE = 32

class Tilemap:
    def __init__(self):
        # Initialize the map and its variations
        self.smooth = [['.'] * ((WIN_WIDTH//TILESIZE)*2)] * ((WIN_HEIGHT//TILESIZE)*2)
        self.map = [['.'] * ((WIN_WIDTH//TILESIZE)*2)] * ((WIN_HEIGHT//TILESIZE)*2)
        
        # Initialize adjacent tilemaps to None
        self.right = None
        self.left = None
        self.top = None
        self.bottom = None
    
    def set_map(self, tile):
        # Set the map using a given tile pattern
        x = ((WIN_HEIGHT//TILESIZE)//2)
        y = ((WIN_WIDTH//TILESIZE)//2)
        for i in range((WIN_HEIGHT//TILESIZE)):
            self.map[i+x] = self.map[i+x][:y] + tile[i] + self.map[i+x][-y:]

        # Create adjacent tilemaps if the current map is not smooth
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
        # Adjust adjacent tilemaps to ensure continuity
        x = ((WIN_HEIGHT//TILESIZE)//2)
        y = ((WIN_WIDTH//TILESIZE)//2)
        height = WIN_HEIGHT//TILESIZE
        width = WIN_WIDTH//TILESIZE
        for i in range(height):
            self.right.map[i+x] =  self.map[i+x][width:width+y] + self.right.map[i+x][y:]
            self.left.map[i+x] = self.left.map[i+x][:width+y] + self.map[i+x][y:width]

        for j in range(x+1):
            self.top.map[j+height+x] = self.top.map[j+height+x][:y] + self.map[x+j][y:width+y] + self.top.map[j+height+x][y+width:]
            self.bottom.map[j] = self.bottom.map[j][:y] + self.map[height+j][y:width+y] + self.bottom.map[j][y+width:]
    
    def set_map_right(self, tilemapp):
        # Set the map to the right using another tilemap
        self.right.set_map(tilemapp)
        self.right.left = self
    
    def set_map_left(self, tilemapp):
        # Set the map to the left using another tilemap
        self.left.set_map(tilemapp)
        self.left.right = self
    
    def set_map_top(self, tilemapp):
        # Set the map to the top using another tilemap
        self.top.set_map(tilemapp)
        self.top.bottom = self
    
    def set_map_bottom(self, tilemapp):
        # Set the map to the bottom using another tilemap
        self.bottom.set_map(tilemapp)
        self.bottom.top = self
# Create a Tilemap instance
Tile = Tilemap()

# Define tilemaps
tilemapp = [
    ['B', 'B', 'B' , 'B', 'B', 'B', 'B', '.', '.', '.', '.', '.', '.', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
    ['B', '.', '.' , '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['B', '.', '.' , '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['B', '.', '.' , '.', '.', '.', '.', '.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['B', '.', '.' , '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['.', '.', '.' , 'B', 'B', 'B', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.' , '.', 'B', '.', '.', '.', '.', 'B', '.', '.', '.', '.', '.', '.', 'B', '.', '.', '.'],
    ['.', '.', '.' , '.', '.', '.', '.', '.', 'B', 'B', 'B', '.', '.', '.', '.', 'B', 'B', 'B', '.', '.'],
    ['.', '.', '.' , '.', '.', '.', 'B', '.', '.', 'B', '.', '.', '.', '.', '.', '.', 'B', '.', '.', '.'],
    ['.', '.', '.' , 'B', 'B', 'B', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['B', '.', '.' , '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['B', '.', '.' , '.', '.', 'B', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['B', '.', '.' , '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['B', '.', '.' , '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'B'],
    ['B', 'B', 'B' , 'B', 'B', 'B', 'B', '.', '.', '.', '.', '.', '.', 'B', 'B', 'B', 'B', 'B', 'B', 'B']
]
Tile.set_map(tilemapp)

# Define tilemaps
tilemapp = [
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
Tile.set_map_bottom(tilemapp)

# Define tilemaps
tilemapp = [
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
Tile.set_map_top(tilemapp)

# Define tilemaps
tilemapp = [
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
Tile.set_map_right(tilemapp)

# Define tilemaps
tilemapp = [
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
Tile.set_map_left(tilemapp)


# Print the final tilemap configuration
for i in Tile.right.left.map:
    for j in i:
        print(j, end='')
    print()
