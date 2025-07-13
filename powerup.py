from turtle import Turtle
import random

class PowerUp(Turtle):
    def __init__(self, shape="circle", color="green"):
        super().__init__()
        self.shape(shape)
        self.color(color)
        self.penup()
        self.speed("fastest")
        self.is_active = False
        self.goto(1000, 1000)
    
    def activate(self):
        """Activate and show the power-up"""
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
        self.is_active = True

    def deactivate(self):
        """Deactivate and hide the power-up"""
        self.is_active = False
        self.goto(1000, 1000)