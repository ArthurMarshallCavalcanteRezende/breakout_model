# Here is the main code to run the "Game"

import ball
import paddle
import keyboard

# Screen sizes

screen_width = 600
screen_height = 700

# Game loop
running_game = True

# Instances
ball_instance = ball.Ball()
paddle_instance = paddle.Paddle()

print("-- Insira S para iniciar o jogo --")
start_game = str(input("Começar o jogo?\n"))

while running_game:
         # Ball variables
        ball_x = ball_instance.x
        ball_y = ball_instance.y

        # Paddle Initial position
        paddle_x = paddle_instance.x
        paddle_y = paddle_instance.y

        # Starting ball movement
        ball_instance.start_moving()
        ball_instance.ball_movement()
        ball_instance.border_collision(screen_width, screen_height, ball_x, ball_y)

        # Player paddle movement
        if keyboard.is_pressed('left') or keyboard.is_pressed('right'):
             paddle_instance.paddle_movement()

        if keyboard.is_pressed('esc'):
            print("Obrigado por jogar.")
            break