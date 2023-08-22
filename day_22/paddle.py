from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape('square')
        self.penup()
        self.seth(90)
        self.goto(x=x, y=y)
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.color('white')

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)

