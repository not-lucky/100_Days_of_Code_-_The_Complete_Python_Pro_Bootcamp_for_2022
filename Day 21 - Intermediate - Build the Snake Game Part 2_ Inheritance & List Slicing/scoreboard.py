from turtle import Turtle

BORDER_PARAMETER = 410
SCORE_POSTION = (0, 412)


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.score = 0
        with open('data.txt') as fl:
            self.high_score = int(fl.read())
        self.write_score()

    def write_score(self):
        self.make_border()
        self.goto(SCORE_POSTION)
        self.write(f'Score: {self.score}  High Score: {self.high_score}',
                   align='center',  font=('Ariel', 24, 'bold'))

    def update_score(self):
        self.clear()
        self.score += 1
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

    def reset(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score

        with open('data.txt', 'w') as fl:
            print(self.high_score, file=fl)

        self.score = 0
        self.write_score()

    # def game_over_screen(self):
    #     self.goto(0, 0)
    #     self.write('GAME OVER', align='center',
    #                font=('Ariel', 24, 'bold'))
