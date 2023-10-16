from turtle import Turtle
NORTH = 90
SOUTH = 270
WEST = 180
EAST = 0


class MySnake:
    def __init__(self, size):
        self.snake = []
        self.create_snake(size)
        self.head = self.snake[0]

    def create_snake(self, size):
        for index in range(size):
            segment = Turtle(shape='square')
            segment.color('white')
            segment.penup()
            segment.goto(x=0-(index * 20), y=0)
            self.snake.append(segment)

    def snake_length(self):
        print(len(self.snake))

    def snake_head_pos(self):
        return self.head.pos()

    def step_forward(self, add_segment):
        if add_segment:
            new_segment = self.snake[-1].clone()
        for index in range(len(self.snake)-1, 0, -1):
            self.snake[index].goto(self.snake[index-1].pos())
            self.snake[index].setheading(self.snake[index-1].heading())
        self.head.forward(20)
        if add_segment:
            self.snake.append(new_segment)

    def add_segment(self):
        segment = self.snake[-1].clone()
        self.snake.append(segment)

    def head_w(self):
        if self.head.heading() != EAST:
            self.head.setheading(WEST)

    def head_n(self):
        if self.head.heading() != SOUTH:
            self.head.setheading(NORTH)

    def head_s(self):
        if self.head.heading() != NORTH:
            self.head.setheading(SOUTH)

    def head_e(self):
        if self.head.heading() != WEST:
            self.head.setheading(EAST)

    def reset_snake(self):
        for segment in self.snake:
            segment.goto(1000, 1000)
        self.snake.clear()
        self.create_snake(3)
        self.head = self.snake[0]
