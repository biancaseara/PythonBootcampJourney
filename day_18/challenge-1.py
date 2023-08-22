from turtle import Turtle, Screen

sangie_the_turtle = Turtle()
sangie_the_turtle.color('maroon')

# times = 4
# while times > 0:
#     sangie_the_turtle.left(90)
#     sangie_the_turtle.forward(100)
#     times -= 1

for _ in range(4):
    sangie_the_turtle.left(90)
    sangie_the_turtle.forward(100)

screen = Screen()
screen.exitonclick()