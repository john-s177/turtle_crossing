FONT = ("Courier", 15, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level=1
        self.penup()
        self.goto(-240,270)
        self.hideturtle()
        self.write(f"Level {self.level}",align="center", font=FONT)

    def level_up(self):
        self.clear()
        self.level+=1
        self.write(f"Level {self.level}",align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align="center", font=FONT)


