import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.title("Turtle Crossing")
screen.onkey(player.up, "Up")

car_manager= CarManager()
scoreboard=Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    if player.ycor()>280:
        player.reset_turtle()
        car_manager.level_up()
        scoreboard.level_up()

    for car in car_manager.all_cars:
        if player.distance(car)<15:
            scoreboard.game_over()
            game_is_on=False

screen.exitonclick()