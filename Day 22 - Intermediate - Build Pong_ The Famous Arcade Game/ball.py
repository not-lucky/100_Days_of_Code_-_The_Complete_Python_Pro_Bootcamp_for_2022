from turtle import Turtle

WIDTH = 30


class Ball(Turtle):
    def __init__(self,) -> None:
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        self.shapesize(stretch_wid=WIDTH/20)
        self.x_move = -4
        self.y_move = 4
        self.ball_speed = 0.005

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_wall(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1
        self.ball_speed *= 0.5
    
    def reset_ball_pos(self):
        self.goto(0,0)
        self.ball_speed = 0.005
        self.x_move *= -1