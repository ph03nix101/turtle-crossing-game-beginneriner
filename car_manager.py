from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        # super().__init__()
        self.cars = []

    def generate_car(self):
        new_car = Turtle("square")
        new_car.shape("square")
        new_car.shapesize(1, 2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.setheading(180)
        new_car.goto(300, random.randint(-260, 260))
        self.cars.append(new_car)

    def car_move(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)
