import random
from turtle import Turtle


POSSIBLE_FOOD_COORDINATES = [-280, -260, -240, -220, -200, -180, -160, -140,
                             -120, -100, -80, -60, -40, -20, 0, 20, 40, 60, 80,
                              100 , 120, 140, 160, 180, 200, 220, 240, 260]


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed(0)
        self.refresh()

    def refresh(self):
        self.goto(random.choice(POSSIBLE_FOOD_COORDINATES),
                  random.choice(POSSIBLE_FOOD_COORDINATES))
