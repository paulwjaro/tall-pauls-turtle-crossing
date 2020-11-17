from turtle import Turtle


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.move_speed = 10
        self.xpos = self.xcor()

    def create_car(self, car_color, car_size, car_speed):
        self.color(car_color)
        self.shapesize(stretch_wid=2, stretch_len=car_size)
        self.move_speed = car_speed

    def move_car(self, move_speed):
        self.forward(move_speed)

    def road_kill(self, player):
        collision_length = self.shapesize()[1] * 20 / 2
        collision_width = self.shapesize()[0] * 20 / 2
        return self.ycor() - collision_width - 20 <= player.ycor() <= self.ycor() + collision_width + 10 and \
            self.distance(player) < collision_length + 15


class Lane:
    def __init__(self):
        self.cars = []
        self.car_length = 5
        self.lane_position = ()
        self.car_dist = 0
        self.car_space = 0

    def create_lane(self, car_lane, car_col, car_qaunt, car_len, car_speed, car_sep):
        self.lane_position = car_lane
        self.car_space = car_sep
        self.car_dist = 0
        for car in range(car_qaunt):
            new_car = Car()
            new_car.create_car(car_col, car_len, car_speed)
            new_car.setposition(self.lane_position)
            new_car.setx(new_car.xcor() + self.car_dist)
            self.car_dist += self.car_space

            self.cars.append(new_car)

    def update_lanes(self, car_lane):
        for car in self.cars:
            car.sety(car_lane[1])


class LaneTime:
    def __init__(self):
        self.lane_speed = 0.1

    def change_speed(self):
        self.lane_speed *= 0.95
