from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.up()
        self.color('white')
        self.left_score = 0
        self.right_score = 0
        self.show_score()
        
    def show_score(self):
        self.clear()
        self.goto((-80, 340))
        self.write(f'{self.left_score}', align='center', font=('Courier', 40, 'bold'))
        self.goto((80, 340))
        self.write(f'{self.right_score}', align='center', font=('Courier', 40, 'bold'))

    def update_score(self):
        self.show_score()

    def increase_lscore(self):
        self.left_score += 1
        self.update_score()
    
    def increase_rscore(self):
        self.right_score += 1
        self.update_score()