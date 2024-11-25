# Here is the main code to run the "Game"

import sys
from modules import game

if __name__ == '__main__':
    # Initializing the game class
    game = game.Game()
    game.reset_game()

    game.run()