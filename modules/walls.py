# Creating wall of blocks
from modules.blocks import Block

class Wall:
    def __init__(self):
        self.brick_list = []


    def remove_brick(self, brick):
        if brick in self.brick_list:
            self.brick_list.remove(brick)

    def create_wall(self, rows=8, columns=14, block_width=60, block_height=10, spacing=5):
        for row in range(rows):
            for column in range(columns):
                x = column * (block_width + spacing)
                y = row * (block_height + spacing)

                # Checking block score
                if y <= 15:
                    points_to_gain = 7
                    speed_increment = 5
                elif y <= 45:
                    points_to_gain = 5
                    speed_increment = 3
                elif y <= 75:
                    points_to_gain = 3
                    speed_increment = 0
                else:
                    points_to_gain = 1
                    speed_increment = 0

                new_block = Block(x, y, points_to_gain, speed_increment)
                self.brick_list.append(new_block)

    def get_block_positions(self):
        return [(block.x, block.y) for block in self.brick_list]