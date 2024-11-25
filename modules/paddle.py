class Paddle:
    def __init__(self):
        self.width = 60
        self.height = 3
        self.speed = 10
        self.x = 300
        self.y = 680

        self.moving_left = False
        self.moving_right = False
        self.shrink = False

        self.collide = None

    def reset(self):
        self.x = 300
        self.y = 680

    def move(self, direction):
        self.collide = None

        if direction == 'left':
            if self.x - self.speed >= 0:
                self.x -= self.speed
            else:
                self.collide = "O jogador está na parede esquerda."
        elif direction == 'right':
            if self.x + self.width + self.speed <= 600:
                self.x += self.speed
            else:
                self.collide = "O jogador está na parede direita."


    def draw(self):
        print('\n||[PADDLE] X: {:03d} | Y: {:03d}'.format(self.x, self.y))
        if self.collide: print(self.collide)

