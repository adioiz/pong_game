import turtle
from random import *


class Ball(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(x=0, y=0)
        self.x = 10
        self.y = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(x=new_x, y=new_y)

    def bounce(self):
        self.y *= -1

    def detect_collision(self):
        if self.xcor() > 380:
            self.reset_position()
            return "l"
        elif self.xcor() < -380:
            self.reset_position()
            return "r"
        elif self.ycor() > 280 or self.ycor() < -280:
            self.bounce()
        return "null"

    def reset_position(self):
        self.goto(0, 0)
        self.x = 10
        # self.color(random_color())



