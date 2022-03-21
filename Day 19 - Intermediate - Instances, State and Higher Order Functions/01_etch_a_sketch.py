from turtle import Turtle, Screen

lucky = Turtle()
screen = Screen()


def move_forward():
    lucky.forward(20)


def move_backward():
    lucky.backward(20)


def clockwise():
    lucky.right(20)


def counterclockwise():
    lucky.left(20)


screen.listen()


def etch():
    screen.onkey(key='w', fun=move_forward)
    screen.onkey(key='s', fun=move_backward)
    screen.onkey(key='d', fun=clockwise)
    screen.onkey(key='a', fun=counterclockwise)
    screen.onkey(key='c', fun=lucky.reset)


etch()
screen.exitonclick()
