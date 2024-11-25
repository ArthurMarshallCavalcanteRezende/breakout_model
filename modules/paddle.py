class Paddle:
    def __init__(self):
        self.width = 100
        self.height = 3
        self.speed = 10
        self.x = 300
        self.y = 680

        self.shrink = False
        self.collide_text = None

    def reset(self):
        self.x = 300
        self.y = 680
        self.width = 100

    def shrink_paddle(self):
        self.width = 20

    def move(self, direction):
        self.collide_text = None

        if direction == 'left':
            if self.x - self.speed >= 0:
                self.x -= self.speed
            else:
                self.collide_text = "O jogador está na parede esquerda."
        elif direction == 'right':
            if self.x + self.width + self.speed <= 600:
                self.x += self.speed
            else:
                self.collide_text = "O jogador está na parede direita."


    def draw(self):
        print('\n||[PADDLE] X: {:03d} | Y: {:03d}'.format(self.x, self.y))
        if self.collide_text: print(self.collide_text)

