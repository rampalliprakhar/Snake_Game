from turtle import Turtle

SPAWN_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]

    def create_snake(self):
        """Create the initial snake"""
        for position in SPAWN_POSITION:
            self.add_snake_part(position)

    def add_snake_part(self, position):
        """Add a new part to the snake"""
        snake_part = Turtle("square")
        snake_part.color("white")
        snake_part.penup()
        snake_part.goto(position)
        self.snake_parts.append(snake_part)

    def reset_snake(self):
        """Reset the snake to its original position"""
        for part in self.snake_parts:
            part.goto(1000, 1000)
        self.snake_parts.clear()
        self.create_snake()
        self.head = self.snake_parts[0]

    def extend_snake(self):
        """Add a new segment to the snake"""
        self.add_snake_part(self.snake_parts[-1].position())

    def move(self):
        """Move the snake's body"""
        for parts in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[parts - 1].xcor()
            new_y = self.snake_parts[parts - 1].ycor()
            self.snake_parts[parts].goto(new_x, new_y)
        self.snake_parts[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def check_wall_collision(self):
        """Check if the snake collides with the wall"""
        if self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280:
            return True
        return False

    def check_body_collision(self):
        """Check if the snake collides with its own body"""
        for part in self.snake_parts[1:]:
            if self.head.distance(part) < 10:
                return True
        return False