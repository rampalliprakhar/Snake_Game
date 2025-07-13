from turtle import Turtle, Screen

class MenuScreen:
    def __init__(self, screen):
        self.screen = screen
        self.menu_turtle = Turtle()
        self.menu_turtle.hideturtle()
        self.menu_turtle.color("white")
        self.menu_turtle.penup()
        self.menu_turtle.speed("fastest")
        self.is_visible = False
        
    def show(self):
        """Display the menu screen"""
        if not self.is_visible:
            self.menu_turtle.goto(0, 50)
            self.menu_turtle.write("SNAKE GAME", align="center", font=("Courier", 32, "bold"))
            
            self.menu_turtle.goto(0, 0)
            self.menu_turtle.write("Press 'ENTER' to Start", align="center", font=("Courier", 20, "normal"))
            
            self.menu_turtle.goto(0, -40)
            self.menu_turtle.write("Use Arrow Keys to Move", align="center", font=("Courier", 16, "normal"))
            
            self.menu_turtle.goto(0, -80)
            self.menu_turtle.write("Avoid obstacles and eat blue food!", align="center", font=("Courier", 14, "normal"))
            
            self.menu_turtle.goto(0, -120)
            self.menu_turtle.write("Green power-ups make you faster!", align="center", font=("Courier", 14, "normal"))
            
            self.is_visible = True
    
    def hide(self):
        """Hide the menu screen"""
        if self.is_visible:
            self.menu_turtle.clear()
            self.is_visible = False
    
    def cleanup(self):
        """Clean up the menu turtle"""
        self.menu_turtle.clear()
        self.menu_turtle.hideturtle()

class GameOverScreen:
    def __init__(self, screen):
        self.screen = screen
        self.game_over_turtle = Turtle()
        self.game_over_turtle.hideturtle()
        self.game_over_turtle.penup()
        self.game_over_turtle.speed("fastest")
        self.is_visible = False
    
    def show(self, score=0, high_score=0):
        """Display the enhanced game over screen with score information"""
        if not self.is_visible:
            # Main "GAME OVER" title
            self.game_over_turtle.goto(0, 100)
            self.game_over_turtle.color("red")
            self.game_over_turtle.write("GAME OVER", align="center", font=("Courier", 36, "bold"))
            
            # Decorative line
            self.game_over_turtle.goto(0, 70)
            self.game_over_turtle.color("white")
            self.game_over_turtle.write("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", align="center", font=("Courier", 12, "normal"))
            
            # Score section
            self.game_over_turtle.goto(0, 40)
            self.game_over_turtle.color("cyan")
            self.game_over_turtle.write(f"FINAL SCORE: {score}", align="center", font=("Courier", 24, "bold"))
            
            # High score section
            self.game_over_turtle.goto(0, 10)
            if score == high_score and score > 0:
                self.game_over_turtle.color("gold")
                self.game_over_turtle.write("🏆 NEW HIGH SCORE! 🏆", align="center", font=("Courier", 20, "bold"))
            else:
                self.game_over_turtle.color("yellow")
                self.game_over_turtle.write(f"High Score: {high_score}", align="center", font=("Courier", 18, "normal"))
            
            # Performance message based on score
            self.game_over_turtle.goto(0, -20)
            performance_msg, performance_color = self.get_performance_message(score)
            self.game_over_turtle.color(performance_color)
            self.game_over_turtle.write(performance_msg, align="center", font=("Courier", 16, "italic"))
            
            # Decorative line
            self.game_over_turtle.goto(0, -50)
            self.game_over_turtle.color("white")
            self.game_over_turtle.write("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", align="center", font=("Courier", 12, "normal"))
            
            # Controls section
            self.game_over_turtle.goto(0, -80)
            self.game_over_turtle.color("lime")
            self.game_over_turtle.write("CONTROLS", align="center", font=("Courier", 18, "bold"))
            
            self.game_over_turtle.goto(0, -110)
            self.game_over_turtle.color("white")
            self.game_over_turtle.write("Press 'R' to Play Again", align="center", font=("Courier", 16, "normal"))
            
            self.game_over_turtle.goto(0, -135)
            self.game_over_turtle.color("white")
            self.game_over_turtle.write("Press 'M' for Main Menu", align="center", font=("Courier", 16, "normal"))
            
            self.game_over_turtle.goto(0, -160)
            self.game_over_turtle.color("white")
            self.game_over_turtle.write("Press 'P' to Pause (during game)", align="center", font=("Courier", 14, "normal"))
            
            # Tip
            self.game_over_turtle.goto(0, -190)
            self.game_over_turtle.color("orange")
            tip = self.get_random_tip()
            self.game_over_turtle.write(f"💡 Tip: {tip}", align="center", font=("Courier", 12, "normal"))
            
            self.is_visible = True
    
    def get_performance_message(self, score):
        """Return a performance message and color based on score"""
        if score == 0:
            return "Better luck next time!", "gray"
        elif score < 5:
            return "Keep practicing!", "orange"
        elif score < 10:
            return "Not bad!", "yellow"
        elif score < 20:
            return "Good job!", "lime"
        elif score < 30:
            return "Excellent!", "cyan"
        elif score < 50:
            return "Amazing!", "magenta"
        else:
            return "LEGENDARY SNAKE MASTER!", "gold"
    
    def get_random_tip(self):
        """Return a random gameplay tip"""
        tips = [
            "Green power-ups make you faster temporarily!",
            "Plan your moves ahead to avoid getting trapped",
            "The game gets faster as your score increases",
            "New obstacles appear every 5 points",
            "Try to create space by moving in large loops",
            "Corner yourself? Try the opposite direction!",
            "Power-ups appear randomly - grab them quick!",
            "Red obstacles are deadly - avoid at all costs!"
        ]
        import random
        return random.choice(tips)

    def hide(self):
        """Hide the game over screen"""
        if self.is_visible:
            self.game_over_turtle.clear()
            self.is_visible = False
    
    def cleanup(self):
        """Clean up the game over turtle"""
        self.game_over_turtle.clear()
        self.game_over_turtle.hideturtle()

class PauseScreen:
    def __init__(self, screen):
        self.screen = screen
        self.pause_turtle = Turtle()
        self.pause_turtle.hideturtle()
        self.pause_turtle.color("yellow")
        self.pause_turtle.penup()
        self.pause_turtle.speed("fastest")
        self.is_visible = False
    
    def show(self):
        """Display the enhanced pause screen"""
        if not self.is_visible:
            self.pause_turtle.goto(0, 200)
            self.pause_turtle.color("black")
            for i in range(20):
                y_pos = 200 - (i * 20)
                self.pause_turtle.goto(-300, y_pos)
                self.pause_turtle.write("█" * 50, align="left", font=("Courier", 8, "normal"))
            
            # Main pause content
            self.pause_turtle.goto(0, 50)
            self.pause_turtle.color("yellow")
            self.pause_turtle.write("⏸️ PAUSED ⏸️", align="center", font=("Courier", 32, "bold"))
            
            self.pause_turtle.goto(0, 0)
            self.pause_turtle.color("white")
            self.pause_turtle.write("Game is temporarily stopped", align="center", font=("Courier", 16, "normal"))
            
            self.pause_turtle.goto(0, -30)
            self.pause_turtle.color("lime")
            self.pause_turtle.write("Press 'P' to Resume", align="center", font=("Courier", 20, "bold"))
            
            self.pause_turtle.goto(0, -60)
            self.pause_turtle.color("orange")
            self.pause_turtle.write("Take a breather and plan your next move!", align="center", font=("Courier", 14, "italic"))
            
            self.is_visible = True
    
    def hide(self):
        """Hide the pause screen"""
        if self.is_visible:
            self.pause_turtle.clear()
            self.is_visible = False
    
    def cleanup(self):
        """Clean up the pause turtle"""
        self.pause_turtle.clear()
        self.pause_turtle.hideturtle()
