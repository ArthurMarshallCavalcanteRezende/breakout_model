# Here is the main code to run the "Game"

import ball
import paddle
import keyboard

# Screen sizes

screen_width = 600
screen_height = 700

# Game loop
running_game = True
game_interval = True

print("-- Aperta a tecla SPACE para iniciar o jogo --")
while running_game:
    if game_interval:
        ball.stop_moving()
    elif keyboard.is_pressed('space'):
        # Starting ball movement
        ball.start_moving()
        ball.ball_movement()
        ball.border_collision()

        # Player paddle movement
        paddle.paddle_movement()

        if keyboard.is_pressed('esc'):
            print("Encerrando o programa.")
            break