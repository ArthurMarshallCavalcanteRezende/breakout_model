import keyboard

class Paddle:
    def __init__(self):
        self.width = 60
        self.height = 3
        self.speed = 10
        self.x = 300
        self.y = 680
        self.left_key_pressed = False
        self.right_key_pressed = False

    def paddle_movement(self):
        if keyboard.is_pressed('left') and not self.left_key_pressed:
            self.left_key_pressed = True
            if self.x - self.speed >= 0:
                self.x -= self.speed
                print(f"O jogador moveu-se para a esquerda, posição = {self.x}")
            else:
                print("O jogador está na parede esquerda.")
        elif not keyboard.is_pressed('left'):
            self.left_key_pressed = False

        if keyboard.is_pressed('right') and not self.right_key_pressed:
            self.right_key_pressed = True
            if self.x + self.width + self.speed <= 600:
                self.x += self.speed
                print(f"O jogador moveu-se para a direita, posição = {self.x}")
            else:
                print("O jogador está na parede direita.")
        elif not keyboard.is_pressed('right'):
            self.right_key_pressed = False

