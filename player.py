from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
FONT = ("Courier", 24, "normal")


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.seth(90)
        self.penup()
        self.go_to_start()

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def reached_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    def go_to_start(self):
        self.goto(STARTING_POSITION)
