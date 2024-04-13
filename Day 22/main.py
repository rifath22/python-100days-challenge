from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

right_paddle = Paddle(380)
left_paddle  = Paddle(-380)
ball         = Ball()
score        = Scoreboard()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

is_on = True
while is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if ball.distance(right_paddle) < 50 and ball.xcor() > 340 or ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    if ball.xcor() > 400:
        score.left_update_score()
        ball.reset_speed()
        ball.goto(0,0)

    if ball.xcor() < -400:
        score.right_update_score()
        ball.reset_speed()
        ball.goto(0,0)

    if score.r_player == 7 or score.l_player == 7:
        is_on = False
        score.game_over()

screen.exitonclick()