from turtle import Turtle, Screen

sangie = Turtle()
sangie.penup()
sangie.backward(200)
sangie.color('dark green')

for _ in range(50):
    sangie.pendown()
    sangie.forward(4)
    sangie.penup()
    sangie.forward(4)

screen = Screen()
screen.exitonclick()