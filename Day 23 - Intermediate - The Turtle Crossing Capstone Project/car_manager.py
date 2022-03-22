from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_LENGTH = 40
CAR_WIDTH = 20


class CarManager():
    def __init__(self):
        self.cars = []
        self.cars_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle()
        new_car.shape('square')
        new_car.penup()
        new_car.setheading(180)
        new_car.color(random.choice(COLORS))
        new_car.shapesize(CAR_WIDTH/20, CAR_LENGTH/20)
        new_car.goto(300, random.randint(-250, 250))
        self.cars.append(new_car)
        
    def move(self):
        for car in self.cars:
            car.forward(self.cars_speed)

    def increase_speed(self):
        self.cars_speed += MOVE_INCREMENT