import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.move, "Up")
counter = 0

game_is_on = True
while game_is_on:
    time.sleep(player.game_speed)
    car.car_move()
    screen.update()

    if counter % 6 == 0:
        car.generate_car()

    for vehicle in car.cars:
        if player.distance(vehicle) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() == player.finish_line_y:
        player.finish_line()
        scoreboard.update_score()

    counter += 1


screen.exitonclick()
