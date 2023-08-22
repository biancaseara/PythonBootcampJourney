from turtle import Turtle, Screen

sangie = Turtle()
screen = Screen()


def move_forward():
    sangie.forward(10)


screen.listen()
screen.onkey(key='space', fun=move_forward)


screen.exitonclick()
