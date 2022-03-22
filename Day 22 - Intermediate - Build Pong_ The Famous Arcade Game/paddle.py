from turtle import Turtle

WIDTH = 20
HEIGHT = 160


class Paddle(Turtle):
    def __init__(self, coordinates) -> None:
        super().__init__()
        self.create(coordinates)
        self.x_coordinate = coordinates[0]

    def create(self, coordinates):
        self.penup()
        self.shape('square')
        self.goto(coordinates)
        self.color('white')
        self.shapesize(stretch_wid=HEIGHT/20, stretch_len=WIDTH/20)

    def up(self):
        self.goto(self.x_coordinate, self.ycor() + 20)

    def down(self):
        self.goto(self.x_coordinate, self.ycor() - 20)
