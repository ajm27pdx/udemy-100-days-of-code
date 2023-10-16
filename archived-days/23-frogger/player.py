from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(15)

    def detect_edge(self):
        if self.ycor() > 280:
            self.sety(-280)
            return True
        else:
            return False

    def reset(self):
        self.goto(STARTING_POSITION)
