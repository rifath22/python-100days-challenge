from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.car_speed = 0.1
        self.create_cars()

    def create_cars(self):
        roll = random.randint(1,6)
        if roll == 1:
            tom = Turtle()
            tom.shape('square')
            tom.color(random.choice(COLORS))
            tom.shapesize(stretch_wid=1, stretch_len=2)
            tom.penup()
            tom.goto(300, random.randint(-250, 250))
            self.cars.append(tom)

    def move(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)
    
    def increase_car_speed(self):
        self.car_speed *= 0.9
