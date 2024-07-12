STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    

    def __init__(self):
        super().__init__()
        self.reset_turtle()

    def reset_turtle(self):
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(0, -280)

    def up(self):
        self.goto(0,self.ycor()+10)

    