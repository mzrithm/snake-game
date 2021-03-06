from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(.5, .5)
        x = randint(-260, 260)
        y = randint(-260, 260)
        self.goto(x, y)
        self.refresh()

    def refresh(self):
        x = randint(-260, 260)
        y = randint(-260, 260)
        self.goto(x, y)



