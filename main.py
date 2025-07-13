import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from powerup import PowerUp
from obstacle import Obstacle
from menu_ui import MenuScreen, GameOverScreen, PauseScreen
import random

# Game states
MENU = "menu"
PLAYING = "playing"
GAME_OVER = "game_over"
PAUSED = "paused"

class SnakeGame:
    def __init__(self):
        # Screen setup
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        self.screen.tracer(0)
        
        # Game objects - initialize but do not display yet
        self.snake = None
        self.food = None
        self.scoreboard = None
        self.power_up = None
        self.obstacles = []
        
        # UI screens
        self.menu_screen = MenuScreen(self.screen)
        self.game_over_screen = GameOverScreen(self.screen)
        self.pause_screen = PauseScreen(self.screen)
        
        # Game state
        self.game_state = MENU
        self.game_speed = 0.1
        
        self.setup_controls()
        self.menu_screen.show()
    
    def setup_controls(self):
        """Setup all game controls"""
        self.screen.listen()
        # Movement controls - these will only work when snake exists
        self.screen.onkey(self.move_up, "Up")
        self.screen.onkey(self.move_down, "Down")
        self.screen.onkey(self.move_left, "Left")
        self.screen.onkey(self.move_right, "Right")
        
        # Game controls
        # Enter to start
        self.screen.onkey(self.start_game, "Return")  
        # R to restart
        self.screen.onkey(self.restart_game, "r")     
        # M for menu
        self.screen.onkey(self.return_to_menu, "m")   
        # P to pause/unpause
        self.screen.onkey(self.toggle_pause, "p")     
    
    def move_up(self):
        if self.snake and self.game_state == PLAYING:
            self.snake.up()
    
    def move_down(self):
        if self.snake and self.game_state == PLAYING:
            self.snake.down()
    
    def move_left(self):
        if self.snake and self.game_state == PLAYING:
            self.snake.left()
    
    def move_right(self):
        if self.snake and self.game_state == PLAYING:
            self.snake.right()
    
    def create_game_objects(self):
        """Create all game objects"""
        self.snake = Snake()
        self.food = Food()
        self.scoreboard = Scoreboard()
        self.power_up = PowerUp()
        
        # Create obstacles
        self.obstacles = [
            Obstacle((100, 100)),
            Obstacle((-150, 50)),
            Obstacle((0, -150)),
        ]
    
    def hide_game_objects(self):
        """Hide all game objects by moving them off-screen"""
        if self.snake:
            for part in self.snake.snake_parts:
                part.goto(1000, 1000)
        
        if self.food:
            self.food.goto(1000, 1000)
        
        if self.scoreboard:
            self.scoreboard.clear()
        
        if self.power_up:
            self.power_up.goto(1000, 1000)
        
        for obstacle in self.obstacles:
            obstacle.goto(1000, 1000)
    
    def show_game_objects(self):
        """Show game objects in their proper positions"""
        if self.snake:
            # Position snake correctly
            self.snake.reset_snake()  
        
        if self.food:
            # Position food correctly
            self.food.refresh(self.snake)  
        
        if self.scoreboard:
            # Display the scoreboard
            self.scoreboard.update_scoreboard()  
        
        if self.power_up:
            # Power-up starts deactivated, will appear randomly during game
            self.power_up.deactivate()
    
    def start_game(self):
        """Start the game from menu"""
        if self.game_state == MENU:
            self.game_state = PLAYING
            self.menu_screen.hide()
            self.create_game_objects()
            self.show_game_objects()
    
    def restart_game(self):
        """Restart the game from game over screen"""
        if self.game_state == GAME_OVER:
            self.game_state = PLAYING
            self.game_over_screen.hide()
            self.show_game_objects()
            self.reset_game_objects()
    
    def return_to_menu(self):
        """Return to main menu"""
        if self.game_state == GAME_OVER:
            self.game_state = MENU
            self.game_over_screen.hide()
            self.hide_game_objects()
            self.menu_screen.show()
    
    def toggle_pause(self):
        """Toggle pause state"""
        if self.game_state == PLAYING:
            self.game_state = PAUSED
            self.pause_screen.show()
        elif self.game_state == PAUSED:
            self.game_state = PLAYING
            self.pause_screen.hide()
    
    def reset_game_objects(self):
        """Reset all game objects to initial state"""
        # If objects do not exist, create them
        if not self.snake:  
            self.create_game_objects()
            
        self.scoreboard.reset_scoreboard()
        self.snake.reset_snake()
        self.food.refresh(self.snake)
        self.power_up.deactivate()
        self.game_speed = 0.1
        
        # Reset obstacles
        for obstacle in self.obstacles:
            # Hide old obstacles
            obstacle.goto(1000, 1000)  
        
        self.obstacles = [
            Obstacle((100, 100)),
            Obstacle((-150, 50)),
            Obstacle((0, -150)),
        ]
    
    def check_game_over(self):
        """Check for game over conditions and handle game events"""
        # Check collision with walls
        if self.snake.check_wall_collision():
            return True

        # Check collision with body
        if self.snake.check_body_collision():
            return True

        # Check if the snake has eaten food
        if self.snake.head.distance(self.food) < 10:
            self.food.refresh(self.snake)
            self.snake.extend_snake()
            self.scoreboard.increase_score()
            self.increase_game_speed()
            self.increase_difficulty()

        # Check if the snake has eaten a power-up
        if self.snake.head.distance(self.power_up) < 15 and self.power_up.is_active:
            self.power_up.deactivate()
            self.game_speed -= 0.02
            self.screen.ontimer(self.reset_game_speed, 5000)
        
        # Check if the snake hits any obstacle
        for obstacle in self.obstacles:
            if self.snake.head.distance(obstacle) < 15:
                return True

        return False

    def increase_game_speed(self):
        """Increase game speed as player progresses"""
        if self.game_speed > 0.05:
            self.game_speed -= 0.005

    def increase_difficulty(self):
        """Add obstacles as difficulty increases"""
        if self.scoreboard.score % 5 == 0 and self.scoreboard.score != 0:
            new_obstacle = Obstacle((random.randint(-250, 250), random.randint(-250, 250)))
            self.obstacles.append(new_obstacle)

    def reset_game_speed(self):
        """Reset game speed after power-up effect"""
        self.game_speed = 0.1

    def end_game(self):
        """Handle game over - hide game objects and show game over screen"""
        # Store the final score before hiding objects
        final_score = self.scoreboard.score
        final_high_score = self.scoreboard.high_score
        
        # Update high score if needed
        if final_score > final_high_score:
            final_high_score = final_score
            self.scoreboard.high_score = final_high_score
            # Save high score to file
            try:
                with open("data.txt", mode="w") as data:
                    data.write(f"{final_high_score}")
            except IOError:
                print("Error saving high score!")
        
        # Hide all game objects first
        self.hide_game_objects()
        
        # Change state and show game over screen
        self.game_state = GAME_OVER
        self.game_over_screen.show(final_score, final_high_score)

    def run(self):
        """Main game loop"""
        try:
            while True:
                if self.game_state == PLAYING:
                    self.screen.update()
                    time.sleep(self.game_speed)
                    self.snake.move()

                    if self.check_game_over():
                        self.end_game()
                else:
                    self.screen.update()
                    time.sleep(0.1)
        except:
            pass

# Create and run the game
if __name__ == "__main__":
    game = SnakeGame()
    game.run()