from turtle import Screen, Turtle
from my_snake import MySnake
from game_brain import GameBrain
import time

score = 0
diff = 8
scale = 0.2
playspace = (600, 600)
# screen = Screen()
# screen.setup(width=playspace[0], height=playspace[1])
# screen.bgcolor('black')
# screen.title('Snake v0.1')
# screen.tracer(0)

# top = Turtle()
# top.color('white')
# top.penup()
# top.hideturtle()
# top.goto((0, playspace[1]/2-30))
# bot = Turtle()
# bot.penup()
# bot.color('white')
# bot.hideturtle()
# bot.goto((0, -playspace[1]/2+30))
#s = MySnake(playspace, 6)

s = Screen()
s.listen()
g = GameBrain(s)
#s.onkey(key='a', fun=g.head_west)
game_running = True
while game_running:
    # s.step_forward()
    # time.sleep(1/diff)
    game_running = g.run()




s.exitonclick()


