import time
from turtle import Screen
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
screen.onkey(player.go_up, 'Up')

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect when the turtle player collides with a car and stop the game if this happens.
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_ends()

    # Detect when the turtle player has reached the top edge of the screen.
    if player.reached_finish_line():
        player.go_to_start()
        car_manager.new_speed()
        scoreboard.new_level()

screen.exitonclick()
