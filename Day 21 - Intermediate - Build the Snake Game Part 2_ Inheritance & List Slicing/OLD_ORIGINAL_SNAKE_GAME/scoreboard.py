from turtle import Turtle

BORDER_PARAMETER = 410
SCORE_POSTION = (0, 412)

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.make_border()
        self.score = 0
        self.goto(SCORE_POSTION)
        self.write_score()

    def write_score(self):
        self.write(f'Score: {self.score}', align='center',
                   font=('Ariel', 24, 'bold'))
                   
    def update_score(self):
        self.clear()
        self.score += 1
        self.make_border()
        self.goto(SCORE_POSTION)
        self.write_score()

    def make_border(self):
        self.penup()
        self.goto(-BORDER_PARAMETER, BORDER_PARAMETER)
        self.pendown()
        self.goto(BORDER_PARAMETER, BORDER_PARAMETER)
        self.goto(BORDER_PARAMETER, -BORDER_PARAMETER)
        self.goto(-BORDER_PARAMETER, -BORDER_PARAMETER)
        self.goto(-BORDER_PARAMETER, BORDER_PARAMETER)
        self.penup()

    def game_over_screen(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center',
                   font=('Ariel', 24, 'bold'))