from turtle import Turtle

UP = 90
DOWN = 270
MOVE_DISTANCE = 20

class Paddle:

    def __init__(self):

        self.create_paddle()


    def create_paddle(self):

        paddle = Turtle('square')
        paddle.color('white')
        paddle.shapesize(stretch_len=1, stretch_wid=5)
        paddle.penup()
        paddle.goto(x=250, y=0)


    def move(self):

        self.paddle.forward(MOVE_DISTANCE)

    def up(self, paddle):

        new_y = paddle.ycor() + 20
        paddle.goto(paddle.xcor(), new_y)

    def down(self, paddle):
        new_y = paddle.ycor() - 20
        paddle.goto(paddle.xcor(), new_y)



