import turtle
import paddle
from ball import Ball
import time
from scoreboard import Scoreboard

STARTING_POSITIONS = [(350, 0), (-350, 0)]
GAME_IS_ON = True
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0) # turn off animations

paddle1 = paddle.Paddle(STARTING_POSITIONS[0])
paddle2 = paddle.Paddle(STARTING_POSITIONS[1])
scoreboard = Scoreboard()

ball = Ball()
screen.listen()
screen.onkey(paddle1.go_up, "Up")
screen.onkey(paddle1.go_down, "Down")
screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")

while GAME_IS_ON:
    time.sleep(ball.move_speed)
    screen.update()  # update the screen
    ball.move()
    if (ball.distance(paddle1) < 40 and ball.xcor() > 335) or (ball.distance(paddle2) < 40 and ball.xcor() < -335):
        ball.x *= -1
        ball.move_speed *= 0.9
    winner = ball.detect_collision()
    if winner == "l":
        ball.move_speed = 0.1
        scoreboard.l_point()
        time.sleep(1)
    elif winner == "r":
        ball.move_speed = 0.1
        scoreboard.r_point()
        time.sleep(1)
    if scoreboard.l_score == 3 or scoreboard.r_score == 3:
        GAME_IS_ON = False
        over = turtle.Turtle()
        over.hideturtle()
        over.penup()
        over.color("white")
        over.write("We have a winner !", align="center", font=("Courier", 30, "normal"))

screen.exitonclick()
