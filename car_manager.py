from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate(self):
        chance = random.randint(1, 6)
        if chance == 1:
            t = Turtle()
            t.shape("square")
            t.color(random.choice(COLORS))
            t.penup()
            t.turtlesize(stretch_wid=1, stretch_len=2)
            y = random.randint(-200, 250)
            t.goto(300, y)
            self.all_cars.append(t)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def levelup(self):
        self.car_speed += MOVE_INCREMENT


