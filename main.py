import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


#Creating the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#creating the player
turtle = Player()
scoreboard = Scoreboard()
#creating keys
screen.listen()
screen.onkey(turtle.move_forward,"Up")

car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #creating and moving cars
    car_manager.create()
    car_manager.move_car()

    #detect collision with the car_manager
    for car in car_manager.cars:
        if car.distance(turtle) < 20:
            game_is_on = False
            scoreboard.game_over()

    #detect successful crossing
    if turtle.is_at_finishline():
        turtle.goto_start()
        car_manager.level_up()
        scoreboard.increase_level()






screen.exitonclick()