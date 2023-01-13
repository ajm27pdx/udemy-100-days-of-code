from turtle import Screen, Turtle
from my_snake import MySnake
import time

diff = 8
scale = 0.2
playspace = (600, 600)
screen = Screen()
screen.setup(width=playspace[0], height=playspace[1])
screen.bgcolor('black')
screen.title('Snake v0.1')
screen.tracer(0)

s = MySnake(playspace, 6)
game_running = True
while game_running:
    s.step_forward()
    game_running = s.detect_wall()
    time.sleep(1/diff)
    screen.update()







screen.exitonclick()
