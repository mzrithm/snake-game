from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.value = 0
        self.high_score = 0
        self.pencolor("white")
        self.hideturtle()
        self.broadcast()

    def count(self, num):
        self.value = self.value + num

    def broadcast(self):
        self.clear()
        self.penup()
        score_message = f"Score: {self.value} High score: {self.high_score}"
        self.setposition(0, 260)
        self.pendown()
        self.write(score_message, False, align="center", font=("Arial", 20, "normal"))

    def reset(self):
        if self.value > self.high_score:
            self.high_score = self.value
        self.value = 0

