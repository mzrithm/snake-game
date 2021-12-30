from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Score
import time


def reset():
    score.reset()
    score.broadcast()
    snake.lost_life()
    response = screen.textinput("Game Over", "Would you like to play again? (Y/N)")
    if response is None:
        snake.died()
    elif response.lower() == "n":
        snake.died()
    else:
        snake.reset()
        play_game()


def play_game():
    game_is_on = True
    screen.listen()
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
            reset()
        if snake.head.ycor() >= 295 or snake.head.ycor() <= -295:
            game_is_on = False
            reset()
        # Detect collision with tail
        for segment in snake.segment_list[1:]:
            # Check every segment except first, aka. the head
            if snake.head.distance(segment) < 10:
                game_is_on = False
                reset()


if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game - @mzrithm")
    screen.tracer(0)
    snake = Snake()
    screen.listen()

    food = Food()
    score = Score()
    score.broadcast()

    play_game()

    screen.exitonclick()
