import turtle


class Paddle(turtle.Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 30
            self.goto(x=self.xcor(), y=new_y)

    def go_down(self):
        if self.ycor() > -250:
            new_y = self.ycor() - 30
            self.goto(x=self.xcor(), y=new_y)