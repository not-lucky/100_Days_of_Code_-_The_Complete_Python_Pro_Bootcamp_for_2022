from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.tracer(0)
blocks = []

snake = Snake()

screen.listen()
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.right, key='Right')
screen.onkey(fun=snake.down, key='Down')

screen.update()
while True:
    screen.update()
    time.sleep(0.05)

    snake.move()


screen.exitonclick()