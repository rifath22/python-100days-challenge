from extract_color import color_list
import random
import turtle
# from turtle import Turtle, Screen

turtle.colormode(255)
tom = turtle.Turtle()

tom.speed('fast')
tom.penup()
tom.right(90)
tom.forward(220)
tom.right(90)
tom.forward(240)
tom.right(180)

for _ in range(10):
    for _ in range(10):
        tom.pencolor(random.choice(color_list))
        tom.pendown()
        tom.dot(20)
        tom.penup()
        tom.fd(50)

    tom.left(90)
    tom.fd(50)
    tom.left(90)
    tom.fd(500)
    tom.right(180)


tom.hideturtle()


screen = turtle.Screen()
screen.exitonclick()