from turtle import Turtle, Screen
import random

lucky = Turtle()
screen = Screen()
screen.colormode(255)
lucky.width(15)
lucky.speed(0)


def face_randomly(my_turtle):
    if random.randint(0, 1) == 0:
        my_turtle.right(random.choice([0, 90, 180, 270]))
    else:
        my_turtle.left(random.choice([0, 90, 180, 270]))


for _ in range(500):
    face_randomly(lucky)
    lucky.color((random.randint(0, 240), random.randint(0, 240), random.randint(0, 240)))
    lucky.forward(30)


screen.exitonclick()
