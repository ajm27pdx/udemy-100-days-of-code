import turtle
from my_snake import MySnake
from food import Food
import time

ALIGN = 'center'
FONT = ('Courier', 18, 'normal')


class GameBrain:
    def __init__(self, screen=turtle.Screen(), area=(600, 600), diff=10):
        self.score = 0
        with open('data.txt', mode='r') as file:
            self.high_score = int(file.read())
        self.init_diff = diff
        self.diff = diff
        self.diff_scale = 0.3
        self.area = area
        self.kill_screen = False
        self.x_boundary = int((self.area[0] / 2) - 20)
        self.y_boundary = int((self.area[1] / 2) - 20)
        self.s = screen
        self.s.tracer(0)
        self.s.listen()
        self.snake = MySnake(3)
        self.init_screen()
        self.t = turtle.Turtle()
        self.b = turtle.Turtle()
        self.c = turtle.Turtle()
        self.init_text()
        self.food = Food(x_loc=self.x_boundary, y_loc=self.y_boundary)
        self.run()
        self.s.exitonclick()

    def init_text(self):
        self.t.color('white')
        self.t.penup()
        self.t.ht()
        self.b.color('white')
        self.b.penup()
        self.b.ht()
        self.t.goto(0, self.area[1] / 2 - 30)
        self.b.goto(0, -self.area[1] / 2 + 30)
        self.c.color('white')
        self.c.penup()
        self.c.ht()
        self.c.goto(0, 0)

    def init_screen(self):
        self.s.setup(width=self.area[0], height=self.area[1])
        self.s.bgcolor('black')
        self.s.title('Snake v0.3')
        self.s.onkeypress(key='a', fun=self.snake.head_w)
        self.s.onkeypress(key='w', fun=self.snake.head_n)
        self.s.onkeypress(key='d', fun=self.snake.head_e)
        self.s.onkeypress(key='s', fun=self.snake.head_s)
        self.s.onkeypress(key='Left', fun=self.snake.head_w)
        self.s.onkeypress(key='Up', fun=self.snake.head_n)
        self.s.onkeypress(key='Right', fun=self.snake.head_e)
        self.s.onkeypress(key='Down', fun=self.snake.head_s)
        self.s.onkeypress(key='r', fun=self.reset)

    def run(self):
        time.sleep(0.25)
        game_continue = True
        add_segment = False
        while game_continue:
            self.snake.step_forward(add_segment)
            add_segment = False
            self.kill_screen = self.detect_wall() or self.detect_tail()
            time.sleep(1/self.diff)
            self.update_text()
            add_segment = self.detect_food()
            self.s.update()
            while self.kill_screen:
                self.show_kill_screen()

    def detect_wall(self):
        if self.snake.snake_head_pos()[0] > self.x_boundary or self.snake.snake_head_pos()[0] < -self.x_boundary:
            # print(f'wall collision at {self.snake.snake_head_pos()}')
            return True
        if self.snake.snake_head_pos()[1] > self.y_boundary or self.snake.snake_head_pos()[1] < -self.y_boundary:
            # print(f'wall collision at {self.snake.snake_head_pos()}')
            return True

        return False

    def detect_tail(self):
        for segment in self.snake.snake:
            if segment != self.snake.head and self.snake.head.distance(segment) < 10:
                return True
        return False

    def detect_food(self):
        if self.snake.snake[0].distance(self.food) < 15:
            self.score += 1
            self.food.hideturtle()
            new_food = Food(x_loc=self.x_boundary, y_loc=self.y_boundary)
            self.food = new_food
            self.diff += self.diff_scale
            self.snake.add_segment()
        else:
            return False

    def update_text(self):
        self.t.clear()
        self.t.write(f'Score: {self.score}', align=ALIGN, font=FONT)
        self.b.clear()
        self.b.write(f'High Score: {self.high_score}', align=ALIGN, font=FONT)
        self.c.clear()

        #self.b.write(f'Debug\nSnake Head - {self.snake.head.pos()}\nFood - {self.food.pos()}\n'
        #             f'Diff - {self.diff:0.1f}\nHeading - {self.snake.head.heading():0.0f}', align=ALIGN, font=FONT)

    def reset(self):
        # TODO: Reset Screen
        self.snake.reset_snake()
        self.kill_screen = False

    def show_kill_screen(self):
        if self.high_score < self.score:
            self.high_score = self.score
            self.b.clear()
            self.b.write(f'New High Score! {self.high_score}', align=ALIGN, font=FONT)
            with open('data.txt', mode='w') as file:
                file.write(f'{self.high_score}')
        self.score = 0
        self.c.clear()
        self.c.write(f'Press [R] to reset', align=ALIGN, font=FONT)
        # TODO: Kill Screen

