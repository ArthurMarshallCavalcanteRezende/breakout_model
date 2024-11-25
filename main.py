# Here is the main code to run the "Game"

import sys
from modules import game

# Screen sizes

screen_width = 600
screen_height = 700

if __name__ == '__main__':
    game = game.Game()

    # Adding other classes to the game class
    game.reset_game()

    game.run()