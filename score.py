from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.value = 0
        self.pencolor("white")
        self.hideturtle()
        self.broadcast()

    def count(self, num):
        self.value = self.value + num

    def broadcast(self):
        self.clear()
        self.penup()
        message = f"Score: {self.value}"
        self.setposition(0, 260)
        self.pendown()
        self.write(message, False, align="center", font=("Arial", 20, "normal"))
