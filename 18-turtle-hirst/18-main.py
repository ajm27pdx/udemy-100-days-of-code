from turtle import Turtle, Screen, colormode
from random import randint, choice


def dashed_line(dist, t):
    traveled = 0
    while traveled < dist:
        t.down()
        t.forward(10)
        t.up()
        t.forward(10)
        traveled += 20


def draw_shape(t, side_len, side_num):
    angle = 360 / side_num
    t.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    for _ in range(side_num):
        t.forward(side_len)
        t.left(angle)


def random_step(t, dist):
    t.pencolor(random_color)
    t.right(90 * randint(0, 4))
    t.forward(dist)


def random_color():
    clr = (randint(0, 255), randint(0, 255), randint(0, 255))
    return clr


def draw_spiro(t, circles):
    drawn = 0
    while drawn < circles:
        t.pencolor(random_color())
        t.circle(100)
        t.right(360 / circles)
        drawn += 1


def hirst_image(t, size, colors, space=30):
    start_loc = -(size * space / 2)
    t.penup()
    t.goto(start_loc - space / 2, start_loc - space / 2)
    t.pendown()
    draw_shape(t, size * space, 4)
    t.penup()
    for row in range(size):
        t.goto(start_loc, start_loc + (space * row))
        for _ in range(size):
            t.dot(15, choice(colors))
            t.fd(space)


turtle = Turtle()
turtle.pensize(1)
turtle.speed(0)
turtle.hideturtle()
colormode(255)

# Hirst Painting
colorscheme = []
for _ in range(10):
    colorscheme.append(random_color())

hirst_image(turtle, 5, colorscheme)

# Spirograph
# draw_spiro(turtle, 25)

# Random Walk
# while True:
#     random_step(turtle, 30)

# Draw Shapes
# for num in range(3, 13):
#     draw_shape(turtle, 100, num)


# Draw Dashed Line
# dashed_line(100, turtle)
# turtle.right(90)
# dashed_line(100, turtle)
# turtle.right(90)
# dashed_line(100, turtle)
# turtle.right(90)
# dashed_line(100, turtle)
# turtle.right(90)

screen = Screen()
screen.exitonclick()


