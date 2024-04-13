from turtle import Turtle, Screen

tom = Turtle()

def forward():
    tom.forward(25)

def backwards():
    tom.backward(25)

def counter_clockwise():
    tom.left(15)

def clockwise():
    tom.right(15)

def clear_drawing():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()

screen = Screen()
screen.listen()
screen.onkey(forward, "w")
screen.onkey(backwards, "s")
screen.onkey(counter_clockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(clear_drawing, "c")
screen.exitonclick()