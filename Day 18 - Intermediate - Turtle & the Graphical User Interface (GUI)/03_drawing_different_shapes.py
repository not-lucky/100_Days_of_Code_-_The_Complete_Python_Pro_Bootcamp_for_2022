from turtle import Turtle, Screen
from random import randint as ri

lucky = Turtle()
screen = Screen()
screen.colormode(255)
lucky.width(5)

for i in range(3, 11):
    lucky.color((ri(0, 255), ri(0, 255), ri(0, 255)))
    for _ in range(i):
        lucky.forward(100)
        lucky.right(round(360/i, 4))

screen.exitonclick()
