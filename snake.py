from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
class Snake:

    def __init__(self):
        self.segments = []
        self.position = 0
        self.create_snake()
    def create_snake(self):
        for postion in STARTING_POSITION:
            self.add_segment(postion)

    def add_segment(self, position):
        tim = Turtle("square")
        tim.penup()
        tim.color("white")
        tim.goto(position)
        self.segments.append(tim)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)
    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)