from turtle import Turtle, Screen

my_turtle = Turtle()
screen = Screen()

# Etch-a-sketch
screen.listen()
screen.exitonclick()


def move_forward():
    my_turtle.forward(5)


def move_backwards():
    my_turtle.backward(5)


def turn_cw():
    my_turtle.right(5)


def turn_ccw():
    my_turtle.left(5)


def reset_screen():
    screen.reset()


screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=turn_ccw)
screen.onkeypress(key="d", fun=turn_cw)
screen.onkeypress(key="c", fun=reset_screen)

