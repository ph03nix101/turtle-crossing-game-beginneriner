from turtle import Turtle

MOVE_DISTANCE = 10
STARTING_POSITION = (0, -280)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_player()
        self.game_speed = 0.1
        self.finish_line_y = 280

    def create_player(self):
        self.shape("turtle")
        self.penup()
        self.color("green")
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def finish_line(self):
        self.goto(STARTING_POSITION)
        self.game_speed *= 0.70
