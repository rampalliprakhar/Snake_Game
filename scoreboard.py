from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("data.txt") as data:
                self.high_score = int(data.read())
        except (FileNotFoundError, ValueError):
            # Fallback if the file is missing or corrupted
            self.high_score = 0  
        self.color("white")
        self.penup()
        self.goto(0, 268)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the displayed score"""
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increase the score and update the scoreboard"""
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset_scoreboard(self):
        """Reset the score and update the high score"""
        if self.score > self.high_score:
            self.high_score = self.score
            try:
                with open("data.txt", mode="w") as data:
                    data.write(f"{self.high_score}")
            except IOError:
                print("Error saving high score!")
        self.score = 0
        self.update_scoreboard()