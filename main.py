from turtle import Screen
from player import Player
from carmanager import LaneTime, Lane
from scoreboard import Scoreboard
import time
import random


# Setup Screen and Game Conditions
screen = Screen()
lanetime = LaneTime()
screen.setup(width=600, height=600)
screen.title("Tall Paul's Turtle Crossing")
screen.bgcolor("springgreen")
screen.tracer(0)
screen.listen()
in_game = True

LANES = [(-300, -180), (-300, -90), (-300, 0), (-300, 90), (-300, 180)]
COLORS = ["orange", "mediumpurple", "crimson", "gold", "royalblue"]
lane_setup = [(3, 5, 4, 284), (5, 2.5, 5, 140), (5, 2.5, 5, 140), (4, 3, 6, 175), (4, 3, 6, 175)]
# random.shuffle(LANES)
random.shuffle(COLORS)
random.shuffle(lane_setup)


# Setup Scoreboard and Game Over Text
score = Scoreboard()


def quit_game():
    global in_game
    in_game = False


def update_level(setup):
    if setup:
        for i in range(len(LANES)):
            lane = Lane()
            lane.create_lane(LANES[i], COLORS[i], *lane_setup[i])
            lane_list.append(lane)
    else:
        random.shuffle(LANES)
        for lane in range(len(lane_list)):
            lane_list[lane].update_lanes(LANES[lane])
        lanetime.change_speed()


# Setup Player and Player Key Bindings
player = Player()
screen.onkey(key="w", fun=player.move_player)

screen.onkey(key="q", fun=quit_game)

lane_list = []

update_level(True)

while in_game:
    screen.update()
    score.write_level()
    # move cars
    for lanes in range(len(lane_list)):
        for cars in range(len(lane_list[lanes].cars)):
            current_car = lane_list[lanes].cars[cars]
            if current_car.road_kill(player):
                player.dead = True
                player.color("red")
                for lanez in range(len(lane_list)):
                    for carz in range(len(lane_list[lanez].cars)):
                        current_car = lane_list[lanez].cars[carz]
                        current_car.hideturtle()
                game_over = Scoreboard()
                game_over.game_over()
            else:
                current_car.move_car(current_car.move_speed)

            if current_car.xcor() > 300 + (current_car.shapesize()[1] * 20):
                current_car.setx((LANES[lanes][0]) - (current_car.shapesize()[1] * 20))

    if player.reset_player():
        player.setposition(player.start_pos)
        score.update_level()
        update_level(False)
        score.clear()
    time.sleep(lanetime.lane_speed)
