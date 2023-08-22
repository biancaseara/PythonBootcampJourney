from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title('My Snake Game')
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.down, key='Down')
screen.onkey(fun=snake.right, key='Right')
screen.onkey(fun=snake.left, key='Left')

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.06)    
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 40:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        is_game_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()

screen.exitonclick()
