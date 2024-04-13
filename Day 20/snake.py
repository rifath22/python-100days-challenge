from turtle import Turtle
MOVE_DISTANCE = 20
UP            = 90
DOWN          = 270
RIGHT         = 0
LEFT          = 180

class Snake():
    x = 20
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for _ in range(3):
            tom = Turtle(shape='square')
            tom.color('white')
            tom.penup()
            self.x = self.x - 20
            tom.goto(self.x, 0)
            self.segments.append(tom)
    
    def move(self):
        for segment in range(len(self.segments) -1, 0, -1):
            new_x_cor = self.segments[segment - 1].xcor()
            new_y_cor = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x_cor, new_y_cor)
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)