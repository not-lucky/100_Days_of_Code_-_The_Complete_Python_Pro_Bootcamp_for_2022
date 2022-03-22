from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

screen = Screen()
screen.bgcolor('black')
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)


right_paddle = Paddle((480, 0))
left_paddle = Paddle((-488, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

screen.listen()

while True:
    screen.update()
    ball.move()
    time.sleep(ball.ball_speed)
    # time.sleep(1)

    if ball.ycor() > 380 or ball.ycor() < -375:
        ball.bounce_wall()

    if (ball.xcor() > 455 and ball.distance(right_paddle) < 84) or (ball.xcor() < -463 and ball.distance(left_paddle) < 84):
        ball.bounce_paddle()

    if ball.xcor() > 465:
        ball.reset_ball_pos()
        scoreboard.increase_lscore()

    if ball.xcor() < -473:
        ball.reset_ball_pos()
        scoreboard.increase_rscore()

screen.exitonclick()
