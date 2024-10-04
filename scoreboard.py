from turtle import Turtle
ALIGMENT = "center"
FONT = ('Courier', 24, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.times_move = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.score_adding()


    def score_adding(self):
        self.clear()
        self.write(f'Score: {self.times_move}', font=FONT, align=ALIGMENT)
        self.times_move += 1
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=FONT, align=ALIGMENT)