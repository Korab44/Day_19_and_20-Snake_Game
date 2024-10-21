from turtle import Turtle
ALIGMENT = "center"
FONT = ('Courier', 24, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.score_adding()


    def score_adding(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', font=FONT, align=ALIGMENT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.score_adding()
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=FONT, align=ALIGMENT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.score_adding()