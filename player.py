from turtle import Turtle

START_POS = (0, -270)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("mediumslateblue")
        self.penup()
        self.start_pos = START_POS
        self.setheading(90)
        self.shapesize(stretch_wid=1.5)
        self.goto(self.start_pos)
        self.move_speed = 10
        self.dead = False

    def move_player(self):
        if not self.dead:
            self.sety(self.ycor() + self.move_speed)

    def reset_player(self):
        return self.ycor() >= 260
