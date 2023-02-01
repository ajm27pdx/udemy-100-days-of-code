from turtle import Turtle
from random import randint

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        # self.penup()
        self.goto((0, 0))
        self.setheading(randint(0, 360))

    def update_pos(self, dist):
        self.detect_ceil()
        #self.detect_wall()
        self.forward(dist)

    def detect_ceil(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.setheading(-self.heading())

    def detect_wall(self):
        if self.xcor() > 380 or self.xcor() < -380:
            self.setheading(-self.heading() + 180)



    def paddle_bounce(self, angle):
        self.setheading(angle)
