from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")

    def refresh(self, snake):
        """Change the location of the food once the snake collides with it"""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)

        # Ensure food does not spawn inside the snake
        while any(part.distance((random_x, random_y)) < 10 for part in snake.snake_parts):
            random_x = random.randint(-280, 280)
            random_y = random.randint(-280, 280)

        self.goto(random_x, random_y)