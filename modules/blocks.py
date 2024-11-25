# Creating block

class Block:
    def __init__(self, x, y, width=60, height=10):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.broken = False
        self.speed_increment = 5
        self.points = 0

    def draw(self):
        print(f"Block(x={self.x}, y={self.y}, broken={self.broken})")