from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer('0')


right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()

screen.onkey(right_paddle.up, 'Up')
screen.onkey(right_paddle.down, 'Down')

screen.onkey(left_paddle.up, 'w')
screen.onkey(left_paddle.down, 's')

game_is_on = True

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # detect collision with wall

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    else:
        ball.move()

    # detect collision with paddle

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 \
            or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #  detect when right paddle misses the ball

    if ball.distance(right_paddle) > 50 and ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #  detect when left paddle misses the ball

    if ball.distance(left_paddle) > 50 and ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()







screen.exitonclick()