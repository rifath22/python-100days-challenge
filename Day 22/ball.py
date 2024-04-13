from turtle import Turtle

class Ball(Turtle):
    x_move = 10
    y_move = 10
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.move()
        self.ball_speed = 0.1
    
    def move(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor, y_cor)

    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.9
    
    def reset_speed(self):
        self.goto(0,0)
        self.ball_speed = 0.1
        self.bounce_x()