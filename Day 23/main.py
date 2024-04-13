import time
from turtle import Screen
from player import Player, FINISH_LINE_Y, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player          = Player()
car_manager     = CarManager()
score           = Scoreboard()
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True

while game_is_on:
    time.sleep(car_manager.car_speed)
    screen.update()
    car_manager.create_cars()
    car_manager.move()

    for car in car_manager.cars:
        if player.distance(car) < 20:
            score.game_over()
            game_is_on  = False
    
    if player.ycor() >= FINISH_LINE_Y:
        player.goto(STARTING_POSITION)
        score.update_score()
        car_manager.increase_car_speed()

screen.exitonclick()