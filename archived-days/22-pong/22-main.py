from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from random import randint

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
#screen.mode('logo')
score = Turtle()
score.ht()
score.color('white')
score.penup()
score.goto(0, 275)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

r_score = 0
l_score = 0

ball = Ball()

game_running = True


def reset_game(d):
    ball.goto(0, 0)
    ball.setheading(d)

# def stop_game():
#     return False


screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

while game_running:
    time.sleep(1/60)
    score.clear()
    score.write(f'{l_score} : {r_score}')
    screen.update()
    ball.update_pos(10)
    if ball.xcor() > 330 and ball.distance(r_paddle) < 50:
        norm = (ball.ycor() - r_paddle.ycor()) / 50
        print(norm)
        ball.paddle_bounce(norm * 130 + 180)
    if ball.xcor() > 380:
        l_score += 1
        reset_game(randint(130, 231))
    elif ball.xcor() < -380:
        r_score += 1
        reset_game(randint(-50, 51))

screen.exitonclick()
