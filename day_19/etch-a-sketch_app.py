from turtle import Screen, Turtle

sangie = Turtle()
screen = Screen()


def move_forward():
    sangie.forward(10)


def move_backward():
    sangie.backward(10)


def turn_left():
    sangie.left(10)


def turn_right():
    sangie.right(10)


def clear():
    sangie.reset()


screen.listen()
screen.onkeypress(key='w', fun=move_forward)
screen.onkeypress(key='s', fun=move_backward)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=clear)


screen.exitonclick()
