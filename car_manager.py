from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        rand_chance = random.randint(1, 6)
        if rand_chance == 1:
            new_car = Turtle()
            new_car.shape('square')
            new_car.color(random.choice(COLORS))
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.goto(300, random.randint(-240, 240))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def new_speed(self):
        self.car_speed += MOVE_INCREMENT
