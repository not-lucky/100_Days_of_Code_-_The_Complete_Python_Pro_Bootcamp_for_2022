import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=1400, height=800)
colors = ['red', 'blue', 'green', 'black', 'purple', 'orange']
turtles = []
bet = screen.textinput(title='Make a bet.', prompt=f"Which color turtle will win the race?\n{','.join(colors)}")


def make_finish_line():
    line_creator = Turtle('circle')
    line_creator.hideturtle()
    line_creator.up()
    line_creator.width(5)
    line_creator.goto(600, 350)
    line_creator.down()
    line_creator.goto(600, -350)


def turtles_starting_line():
    y_coordinate = -250
    for color in colors:
        colorcolor = Turtle(shape='turtle')
        colorcolor.up()
        colorcolor.color(color)
        colorcolor.speed(0)
        colorcolor.goto(-600, y_coordinate)
        y_coordinate += 100
        turtles.append(colorcolor)


def game():
    turtles_starting_line()
    make_finish_line()

    finish = 600
    while True:
        for turtle in turtles:
            turtle.forward(random.randint(2, 20))
            if turtle.xcor() >= finish:
                if turtle.pencolor() == bet:
                    print(f'You won the bet!! The winning turtle is {turtle.pencolor()}.')
                    return
                else:
                    print(f'You lost the bet!! The winning turtle is {turtle.pencolor()}.')
                    return


game()
screen.exitonclick()
