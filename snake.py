from turtle import Turtle, Screen
from time import sleep

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segment_list = []
        self.segment_size = 20
        self.initial_position = (0, 0)
        self.screen = Screen()
        self.create_snake()
        self.head = self.segment_list[0]

    def create_snake(self):
        for each in range(3):
            x_coord = self.segment_size
            new_snake = Turtle("square")
            new_snake.color("white")
            new_snake.penup()
            x_coord = x_coord - self.segment_size
            new_snake.setposition(x_coord, 0)
            self.segment_list.append(new_snake)

    def move_snake(self):
        size = len(self.segment_list) - 1
        for i in range(size, -1, -1):
            if i == 0:
                self.head.forward(20)
            else:
                new_position = self.segment_list[i - 1].position()
                self.segment_list[i].goto(new_position)

    def grow(self):
        last = self.segment_list[-1].position()
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.setposition(last)
        self.segment_list.append(new_snake)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def quit_snake(self):
        self.screen.bye()

    def direct_snake(self):
        self.screen.onkey(self.turn_up, key="Up")
        self.screen.onkey(self.turn_down, key="Down")
        self.screen.onkey(self.turn_left, key="Left")
        self.screen.onkey(self.turn_right, key="Right")

    def died(self):
        ending = Turtle()
        ending.hideturtle()
        ending.color("white")
        ending.write("GAME OVER", align="center", font=("Arial", 30, "bold"))

    def lost_life(self):
        death = Turtle()
        death.penup()
        death.hideturtle()
        death.color("white")
        death.write("SNAKE DIED", align="center", font=("Arial", 30, "bold"))
        sleep(.5)
        death.clear()
        death.goto(1000, 1000)

    def reset(self):
        for seg in self.segment_list:
            seg.hideturtle()
            seg.goto(1000, 1000)
        self.segment_list.clear()
        self.create_snake()
        self.head = self.segment_list[0]
