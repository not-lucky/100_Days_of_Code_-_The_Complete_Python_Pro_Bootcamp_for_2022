from turtle import Turtle, Screen

lucky = Turtle()
screen = Screen()
for _ in range(4):
    lucky.forward(200)
    lucky.right(90)

screen.exitonclick()
