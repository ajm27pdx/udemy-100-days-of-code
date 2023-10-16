from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
START_POS = 300


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color(COLORS[1])
        self.penup()
        self.goto(START_POS, 0)
        self.cars = []

    def move_cars(self, player):
        for car in self.cars:
            car.forward(car.forward_step)
            if car.xcor() < -300:
                car.setx(START_POS)
            if car.distance(player) < 15:
                return True
        return False

    def spawn_car(self):
        car = Turtle(shape='square')
        car.color(random.choice(COLORS))
        car.penup()
        car.goto(x=315, y=random.randint(-220, 220))
        car.setheading(180)
        car.forward_step = random.randint(3, 10)
        self.cars.append(car)

    def update_screen(self, level, player):
        collision = self.move_cars(player)
        if len(self.cars) < level * 20:
            if random.randint(0, 10) > 5:
                self.spawn_car()
        return collision

    def clear_manager(self, scr):
        for car in self.cars:
            car.ht()
        scr.update()
        self.cars = []
