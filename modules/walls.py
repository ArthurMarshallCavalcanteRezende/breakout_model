# Creating wall of blocks
from modules.blocks import Block

class Wall:
    def __init__(self):
        self.brick_list = []

    def create_wall(self, rows=8, columns=14, block_width=60, block_height=10, spacing=5):
        for row in range(rows):
            for column in range(columns):
                x = column * (block_width + spacing)
                y = row * (block_height + spacing)
                self.brick_list.append(Block(x, y))

    def get_block_positions(self):
        return [(block.x, block.y) for block in self.brick_list if not block.broken]