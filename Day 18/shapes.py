from turtle import Turtle, Screen
import random

color_list = []
for i in range(10):
    one_color = (random.random(), random.random(), random.random())
    color_list.append(one_color)
print(color_list)

turtle = Turtle()

for n in range(3, 10):
    for i in range(n):
        turtle.pencolor(color_list[n])
        turtle.forward(50)
        turtle.left(360/n)

screen = Screen()
screen.exitonclick()