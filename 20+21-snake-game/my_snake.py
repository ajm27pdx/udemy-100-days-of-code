from turtle import Turtle


class MySnake:
    def __init__(self, space):
        self.snake = []
        self.x_boundary = (space[0] / 2) - 20
        self.y_boundary = (space[1] / 2) - 20
        for index in range(3):
            segment = Turtle(shape='square')
            segment.color('white')
            segment.penup()
            segment.goto(x=0-(index * 20), y=0)
            self.snake.append(segment)

    def snake_length(self):
        print(len(self.snake))

    def step_forward(self):
        self.snake[0].setheading(90)
        self.snake[0].forward(20)
        for index in range(len(self.snake)-1, 0, -1):
            self.snake[index].setheading(self.snake[index-1].heading())
            self.snake[index].forward(20)

    def detect_wall(self):
        if self.snake[0].xcor() > self.x_boundary or self.snake[0].xcor() < -self.x_boundary:
            print(f'wall collision at {self.snake[0].pos()}')
            return False
        if self.snake[0].ycor() > self.y_boundary or self.snake[0].ycor() < -self.y_boundary:
            print(f'wall collision at {self.snake[0].pos()}')
            return False

        return True
