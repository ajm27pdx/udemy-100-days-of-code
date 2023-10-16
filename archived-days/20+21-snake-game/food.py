from turtle import Turtle
from random import randrange


class Food(Turtle):
    def __init__(self, x_loc=0, y_loc=0):
        super().__init__()

        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('red')
        self.speed("fastest")
        self.goto(randrange(-x_loc, x_loc, 20), randrange(-y_loc, y_loc, 20),)
