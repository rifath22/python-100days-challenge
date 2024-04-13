from turtle import Turtle, Screen
import random

color_list = []
for i in range(10):
    one_color = (random.random(), random.random(), random.random())
    color_list.append(one_color)
print(color_list)

direction = [90, 270, 180, 360]
turtle = Turtle()
turtle.pensize(10)

for n in range(0, 100):
    pen_color       = random.choice(color_list)
    pen_direction   = random.choice(direction)
    turtle.pencolor(pen_color)
    turtle.forward(50)
    turtle.setheading(pen_direction)

screen = Screen()
screen.exitonclick()