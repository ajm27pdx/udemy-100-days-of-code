from turtle import Turtle
NORTH = 90
SOUTH = 270
WEST = 180
EAST = 0

class MySnake:
    def __init__(self, size):
        self.snake = []

        for index in range(size):
            segment = Turtle(shape='square')
            segment.color('white')
            segment.penup()
            segment.goto(x=0-(index * 20), y=0)
            self.snake.append(segment)

    def snake_length(self):
        print(len(self.snake))

    def snake_head_pos(self):
        return self.snake[0].pos()

    def step_forward(self):
        self.snake[0].forward(20)
        for index in range(len(self.snake)-1, 0, -1):
            self.snake[index].forward(20)
            self.snake[index].setheading(self.snake[index-1].heading())

    def head_w(self):
        if self.snake[0].heading() != EAST:
            self.snake[0].setheading(WEST)
        print('west')

    def head_n(self):
        if self.snake[0].heading() != SOUTH:
            self.snake[0].setheading(NORTH)
        print('north')

    def head_s(self):
        if self.snake[0].heading() != NORTH:
            self.snake[0].setheading(SOUTH)
        print('south')

    def head_e(self):
        if self.snake[0].heading() != WEST:
            self.snake[0].setheading(EAST)
        print('east')
