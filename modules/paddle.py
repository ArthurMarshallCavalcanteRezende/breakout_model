# Paddle mechanics
import keyboard

class paddle:
    def __init__(self):
        self.width = 5
        self.height = 3
        self.speed = 5
        self.x = 0

    def paddle_movement(self, x):
        player_position = x
        if keyboard.is_pressed('left'):
            print("O jogador moveu-se para a esquerda.")
            player_position -= self.speed

        elif keyboard.is_pressed('right'):
            print("O jogador moveu-se para a direita.")
            player_position += self.speed