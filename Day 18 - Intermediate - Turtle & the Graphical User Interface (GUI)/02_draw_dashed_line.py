from turtle import Turtle, Screen

lucky = Turtle()
screen = Screen()

for _ in range(15):
    lucky.forward(15)
    lucky.up()
    lucky.forward(15)
    lucky.down()

screen.exitonclick()
