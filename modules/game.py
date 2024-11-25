# Here is the main code to run the "Game"
import time
import keyboard
import os

from modules import ball
from modules import paddle
from modules import score

# "Game" is a class, and serves access to all variables inside it along with the main loop
class Game:
    def __init__(self):
        # Screen sizes
        self.screen_width = 600
        self.screen_height = 700
        self.FPS = 60
        self.tick = 0

        # Game loop
        self.running = True
        self.on_menu = True

        # Classes (they are added in "main")
        self.ball = ball.Ball()
        self.paddle = paddle.Paddle()
        self.score = score.Score()

        # Text information to print
        self.clear_space_text = 8 * '\n'

    def reset_game(self):
        print(self.clear_space_text)
        print('---------- MENU ----------')
        self.score.draw()
        print('\n- Aperte ENTER para iniciar')

        self.score.reset()
        self.ball.reset()
        self.on_menu = True

    def run(self):
        # Starting ball movement
        frame_duration = 1 / self.FPS

        while self.running:
            self.tick += 1

            # making sure the game runs at 60 frames per second
            start_time = time.time()
            elapsed_time = time.time() - start_time

            if elapsed_time < frame_duration:
                time.sleep(frame_duration - elapsed_time)

            self.handle_events()

            if not self.on_menu:
                self.update_game()

            self.draw()


    def handle_events(self):
        # Player paddle movement
        if self.on_menu:
            if keyboard.is_pressed('enter'):
                self.on_menu = False
                self.ball.toggle_movement(True)

        else:
            if keyboard.is_pressed('left'):
                 self.paddle.move('left')
            if keyboard.is_pressed('right'):
                 self.paddle.move('right')


        if keyboard.is_pressed('esc'):
            print("Encerrando o programa.")
            self.running = False

    def update_game(self):
        # Finishing game if needed
        attempts = self.score.attempts
        if attempts >= 4: self.reset_game()

        # Updating the ball and checking collisions
        self.ball.update()
        self.ball.border_collision(self, self.screen_width, self.screen_height)


    def draw(self):
        # Atualizando "tela" lentamente
        if self.tick % 15 == 0:
            if not self.on_menu:
                print(self.clear_space_text)

                print('----- BREAKOUT MODEL -----')
                self.score.draw()
                self.ball.draw()
                self.paddle.draw()