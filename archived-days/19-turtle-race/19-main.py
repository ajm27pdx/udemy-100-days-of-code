from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
screen.listen()

# Turtle Race
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_bet = screen.textinput(title="Make your bet", prompt="Enter a color: ")
turtles = []
finish_line = 200


def draw_finish():
    t = Turtle(shape="square")
    t.penup()
    for row in range(12):
        t.goto(finish_line - (row % 2) * 20, 100 - (row * 20))
        t.stamp()
        t.goto((finish_line - 40) - (row % 2) * 20, 100 - (row * 20))
        t.stamp()


def init_turts(num):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[num])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + (num * 40))
    return new_turtle


draw_finish()

for index in range(6):
    turtles.append(init_turts(index))

racing = True
winner = ""
while racing:
    for turtle in turtles:
        turtle.forward(randint(0, 10))
        if turtle.xcor() > finish_line:
            winner = turtle.pencolor()
            racing = False

print(f"{winner} finished first!")
if user_bet == winner:
    print(f"You won the bet!")
else:
    print(f"You lost the bet :(")
screen.exitonclick()

# # Etch-a-sketch
#
#
# def move_forward():
#     my_turtle.forward(5)
#
#
# def move_backwards():
#     my_turtle.backward(5)
#
#
# def turn_cw():
#     my_turtle.right(5)
#
#
# def turn_ccw():
#     my_turtle.left(5)
#
#
# def reset_screen():
#     screen.reset()
#
#
# screen.onkeypress(key="w", fun=move_forward)
# screen.onkeypress(key="s", fun=move_backwards)
# screen.onkeypress(key="a", fun=turn_ccw)
# screen.onkeypress(key="d", fun=turn_cw)
# screen.onkeypress(key="c", fun=reset_screen)
#
# screen.exitonclick()
