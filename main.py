from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()

game_is_on = True

food = Food()
score = Score()
score.broadcast()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.direct_snake()
    snake.move_snake()
    # Detect collision with food
    if snake.head.distance(food) <= 20:
        food.refresh()
        snake.grow()
        score.count(1)
        score.broadcast()
    # Detect collision with wall
    if snake.head.xcor() >= 295 or snake.head.xcor() <= -295:
        game_is_on = False
    if snake.head.ycor() >= 295 or snake.head.ycor() <= -295:
        game_is_on = False
    # Detect collision with tail
    for segment in snake.segment_list[1:]:
    #Check every segment except first, aka. the head
        if snake.head.distance(segment) < 10:
            game_is_on = False

snake.died()
screen.exitonclick()
