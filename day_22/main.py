from scoreboard import Scoreboard
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')

r_paddle = Paddle(x=360, y=0)
l_paddle = Paddle(x=-360, y=0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key='Up', fun=r_paddle.up)
screen.onkeypress(key='Down', fun=r_paddle.down)
screen.onkeypress(key='w', fun=l_paddle.up)
screen.onkeypress(key='s', fun=l_paddle.down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    if ball.xcor() > 380:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.l_point()

    if ball.xcor() < -390:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.r_point()
    
screen.exitonclick()
