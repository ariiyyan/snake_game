from turtle import Turtle
STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segmnet = []
        self.creat_snake()
        self.head = self.segmnet[0]

    def creat_snake(self):

        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segmnet.append(new_segment)

    def extend(self):
        #add segment to snake
        self.add_segment(self.segmnet[-1].position())





    def move(self):
        for seg_num in range(len(self.segmnet) - 1, 0, -1):
            new_x = self.segmnet[seg_num - 1].xcor()
            new_y = self.segmnet[seg_num - 1].ycor()
            self.segmnet[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()  != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


