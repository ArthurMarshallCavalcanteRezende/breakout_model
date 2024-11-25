# Creating block

class Block:
    def __init__(self, x, y, points_to_gain, speed_increment, width=60, height=10):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.speed_increment = speed_increment
        self.points_to_gain = points_to_gain

    def draw(self):
        print(f"Block(x={self.x}, y={self.y}")