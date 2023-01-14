import turtle
from my_snake import MySnake
import time


class GameBrain:
    def __init__(self, screen, area=(600, 600), diff=8):
        self.score = 0
        self.diff = diff
        self.area = area
        self.s = screen
        self.init_screen()
        self.t = turtle.Turtle()
        self.b = turtle.Turtle()
        self.init_text()
        self.snake = MySnake(3)
        self.s.onkey(key='a', fun=self.snake.head_w)
        self.s.onkey(key='w', fun=self.snake.head_n)
        self.s.onkey(key='d', fun=self.snake.head_e)
        self.s.onkey(key='s', fun=self.snake.head_s)
        self.x_boundary = (self.area[0] / 2) - 20
        self.y_boundary = (self.area[1] / 2) - 20

    def init_text(self):
        self.t.color('white')
        self.t.penup()
        self.t.ht()
        self.b.color('white')
        self.b.penup()
        self.b.ht()
        self.t.goto(0, self.area[1] / 2 - 30)
        self.b.goto(0, -self.area[1] / 2 + 30)
        self.t.write('test', align='center')
        self.b.write('test', align='center')

    def init_screen(self):
        self.s.setup(width=self.area[0], height=self.area[1])
        self.s.bgcolor('black')
        self.s.title('Snake v0.1')
        self.s.tracer(0)

    def run(self):
        game_continue = True
        self.snake.step_forward()
        game_continue = self.detect_wall()
        time.sleep(1/self.diff)
        if game_continue:
            self.s.update()
        return game_continue

    def detect_wall(self):
        if self.snake.snake_head_pos()[0] > self.x_boundary or self.snake.snake_head_pos()[0] < -self.x_boundary:
            print(f'wall collision at {self.snake.snake_head_pos()}')
            return False
        if self.snake.snake_head_pos()[1] > self.y_boundary or self.snake.snake_head_pos()[1] < -self.y_boundary:
            print(f'wall collision at {self.snake.snake_head_pos()}')
            return False

        return True

