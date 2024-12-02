class ScreenWalls:
    def __init__(self):
        self.width = 1
        self.height = 700
        self.x = 0
        self.y = 0

    def draw(self, position):
        if position == "LEFT":
            print("Left wall created!")
            self.x = 1
        elif position == "RIGHT":
            print("Right wall created!")
            self.x = 700
        elif position == "UP":
            print("Top border created!")
            self.x = 350
            self.y = 700

