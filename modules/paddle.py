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
            if player_position <= -300:
                print("O jogador está na parede esquerda.")
            else:
                print("O jogador moveu-se para a esquerda.")
                player_position -= self.speed

        elif keyboard.is_pressed('right'):
            if player_position >= 300:
                print("O jogador está na parede direita.")
            else:
                print("O jogador moveu-se para a direita.")
                player_position += self.speed