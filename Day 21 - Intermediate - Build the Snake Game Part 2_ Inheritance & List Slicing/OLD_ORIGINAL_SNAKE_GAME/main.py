from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard



screen = Screen()
screen.bgcolor('black')
screen.setup(width=900, height=900)
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.right, key='Right')
screen.onkey(fun=snake.down, key='Down')


def game():
    while True:
        screen.update()
        time.sleep(0.05)

        snake.move()

        if snake.FIRST_BLOCK.distance(food) < 10:
            food.refresh()
            snake.grow_bigger()
            scoreboard.update_score()

        if snake.FIRST_BLOCK.xcor() > 410 or snake.FIRST_BLOCK.xcor() < -410  or snake.FIRST_BLOCK.ycor() > 410  or snake.FIRST_BLOCK.ycor() < -410:
            scoreboard.game_over_screen()
            break

        for block in snake.blocks[1:]:
            if snake.FIRST_BLOCK.distance(block) < 10:
                scoreboard.game_over_screen()
                return


game()


screen.exitonclick()
