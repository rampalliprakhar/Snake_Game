from turtle import Turtle

class Obstacle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("red")
        self.penup()
        self.goto(position)