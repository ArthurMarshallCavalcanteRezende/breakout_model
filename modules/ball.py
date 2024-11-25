class Ball:
    def __init__(self, width=3, height=3, speed_x=5, speed_y=5):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.moving = False

    def start_moving(self):
        self.moving = True

    def stop_moving(self):
        self.moving = False

    def ball_movement(self):
        if self.moving:
            ball_x = self.x + self.speed_x
            ball_y = self.y + self.speed_y
            return ball_x, ball_y, "A bola se movimenta para ({}, {}).".format(ball_x, ball_y)
        return self.x, self.y, "A bola está parada."

    def border_collision(self, max_width, max_height, ball_x, ball_y):
        new_speed_x = self.speed_x
        new_speed_y = self.speed_y

        if ball_x <= 0 or ball_x + self.width >= max_width:
            new_speed_x *= -1
        if ball_y <= 0 or ball_y + self.height >= max_height:
            new_speed_y *= -1

        collided = (new_speed_x != self.speed_x or new_speed_y != self.speed_y)
        if collided:
            return new_speed_x, new_speed_y,
        return new_speed_x, new_speed_y,
