from turtle import Turtle

FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-230, 265)
        self.level = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Level: {self.level}', align='center', font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER', align='center', font=FONT)