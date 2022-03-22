import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


lucky = Player()
carmanager = CarManager()
scoreboard = Scoreboard()
screen.onkey(lucky.move, 'Up')
screen.listen()


game_is_on = True

def game():
    loop_run_counter = 0
    while game_is_on:
        time.sleep(0.1)
        screen.update()

        for car in carmanager.cars:
            if car.distance(lucky) < 23:
                scoreboard.game_over()
                return
        
        if loop_run_counter % 6 == 0:
            carmanager.create_car()

        carmanager.move()

        if lucky.ycor() > FINISH_LINE_Y:
            scoreboard.increase_level()
            lucky.back_to_bog()
            carmanager.increase_speed()

        loop_run_counter += 1


game()
screen.exitonclick()