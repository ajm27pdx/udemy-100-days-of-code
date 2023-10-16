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

    def set_level(self, rec_level):
        self.level = rec_level
        self.clear()
        self.write(f'Level: {self.level}', font=FONT)

    def kill_screen(self):
        self.goto(0,0)
        self.write(f'Game Over', align='center', font=FONT)

    def clear_killscreen(self):
        self.clear()
        self.goto(-260, 260)
        self.set_level(1)
