from turtle import Turtle, Screen
import random
turtle_names = ["violet", "blue", "green", "yellow", "orange", "red"]

screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput("Turtle Graphics", "Choose your turtle:")
print(user_input)

y = -180
turtle_list = []
is_race_on = True

for color_values in turtle_names:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color_values)
    new_turtle.penup()
    y = y + 50
    new_turtle.goto(-220, y)
    turtle_list.append(new_turtle)

while is_race_on:
    for turtles in turtle_list:
        if turtles.xcor() > 200:
            is_race_on = False
            if user_input == turtles.pencolor():
                print(f"You won! The winner is {turtles.pencolor()}")
            else:
                print(f"You lose! The winner is {turtles.pencolor()}")
        random_distance = random.randint(0,10)
        turtles.forward(random_distance)


screen.exitonclick()