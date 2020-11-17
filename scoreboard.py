from turtle import Turtle

START_POS = (-260, 260)
FONT = ("arial", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("darkslateblue")
        self.penup()
        self.hideturtle()
        self.setposition(START_POS)
        self.level = 0

    def write_level(self):
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", align="center", font=('arial', 30, "normal"))
        self.sety(self.ycor() - 100)
        self.write("Press 'Q' to Quit", align="center", font=FONT)

    def update_level(self):
        self.level += 1
