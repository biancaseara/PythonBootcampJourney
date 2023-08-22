from turtle import Turtle, Screen
import random as r

colors = ['cornflower blue', 'green yellow', 'brown', 'purple', 'olive', 'orange red', 'crimson', 'navy', 'dodger blue']

sangie = Turtle()


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        sangie.forward(100)
        sangie.left(angle)


for shape_side_n in range(3, 11):
    sangie.color(r.choice(colors))
    draw_shape(shape_side_n)

# sangie.shape('turtle')
# sangie.color('indigo')
# sangie.forward(200)
# sangie.left(90)
# clone = sangie.clone()
# clone.backward(50)
# clone.write('Second Life!', True, align='left', font=('Ariel', 12, 'normal'))
# clone.forward(50)

screen = Screen()
screen.exitonclick()