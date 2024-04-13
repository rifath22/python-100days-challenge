from turtle import Turtle, Screen
import random

color_list = []
for i in range(10):
    one_color = (random.random(), random.random(), random.random())
    color_list.append(one_color)
print(color_list)

turtle = Turtle()
turtle.speed('fastest')
# turtle.pensize(10)
movement = 10
for n in range(0, int(360/movement)):
    pen_color       = random.choice(color_list)
    turtle.pencolor(pen_color)
    turtle.circle(50)
    turtle.left(movement)

screen = Screen()
screen.exitonclick()