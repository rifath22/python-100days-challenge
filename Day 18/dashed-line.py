import imp
from turtle import Turtle, Screen

tom = Turtle()

for _ in range(10):
    tom.forward(20)
    tom.penup()
    tom.forward(20)
    tom.pendown()


screen = Screen()
screen.exitonclick()
