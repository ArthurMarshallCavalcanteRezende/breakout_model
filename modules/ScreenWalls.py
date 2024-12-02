class ScreenWalls:
    def __init__(self):
        self.width = 1
        self.height = 700
        self.x = 1
        self.y = 5

    def draw(self, position):
        if position == "LEFT":
            print("Left wall created!")
        elif position == "RIGHT":
            print("Right wall created!")
        elif position == "UP":
            print("Top border created!")

