from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.shape('square')
        self.speed('fastest')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x, 0)
    
    def up(self):
        new_x = self.xcor()
        new_y = self.ycor() + 20
        self.goto(new_x, new_y)

    def down(self):
        new_x = self.xcor()
        new_y = self.ycor() - 20
        self.goto(new_x, new_y)
