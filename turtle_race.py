from turtle import Turtle
import random

class TurtleRace:
    def __init__(self):
        self.colors = ["red", "green", "blue", "purple", "yellow"]
        self.all_tim = self.setup_race()
        self.winner = None

    def setup_race(self):
        all_tim = []
        for color_index in range(5):
            y = 100 - 50 * color_index
            tim = Turtle(shape="turtle")
            tim.penup()
            tim.color(self.colors[color_index])
            tim.goto(-230, y)
            all_tim.append(tim)
        return all_tim

    def run_race(self):
        race_on = True
        while race_on:
            for turtle in self.all_tim:
                if turtle.xcor() > 230:
                    self.winner = turtle.pencolor()
                    race_on = False
                rand_distance = random.randint(0, 10)
                turtle.forward(rand_distance)
