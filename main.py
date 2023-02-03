import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

flag = True
while flag:
    time.sleep(0.1)
    screen.update()

    car_manager.generate()
    car_manager.move()

    # detect collision with car
    for car in  car_manager.all_cars:
        if car.distance(player) < 20:
            flag = False
            scoreboard.over()

    # detect crossing successful
    if player.crossed():
        player.start()
        car_manager.levelup()
        scoreboard.increase()

screen.exitonclick()