from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-260, 260)
        self.color('black')
        self.write(f'Level: {self.level}', font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f'Level: {self.level}', font=FONT)