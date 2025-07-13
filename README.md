# Snake Game

- A modern, feature-rich implementation of the classic Snake game built with Python's Turtle graphics library.
- Experience smooth gameplay, progressive difficulty, power-ups, and a polished user interface.

## Features

### Core Gameplay
- **Classic Snake Mechanics**: Control your snake to eat food and grow longer
- **Smooth Controls**: Responsive arrow key movement with collision prevention
- **Progressive Difficulty**: Game speed increases as your score grows
- **Dynamic Obstacles**: New red obstacles appear every 5 points for added challenge

### Power-ups & Bonuses
- **Speed Boost Power-ups**: Green circles that temporarily increase game speed
- **Smart Food Placement**: Food never spawns inside the snake's body
- **Score System**: Real-time scoring with persistent high score tracking

### User Interface
- **Professional Menu System**: Clean, informative main menu
- **Enhanced Game Over Screen**: Detailed performance feedback and tips
- **Pause Functionality**: Pause/resume game anytime with 'P' key
- **Visual Feedback**: Color-coded UI elements and performance messages

### Technical Features
- **Persistent High Scores**: Automatically saves and loads your best score
- **Modular Architecture**: Clean, organized code structure
- **Error Handling**: Graceful handling of file operations and window events
- **Optimized Performance**: Efficient game loop and object management

## Quick Start

### Prerequisites
- Python 3.7 or higher

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/snake-game.git
   cd snake-game
   ```

2. **Run the game**
   ```bash
   python main.py
   ```

The game will launch immediately.

## How to Play

### Basic Controls
- **Arrow Keys**: Move the snake (Up, Down, Left, Right)
- **Enter**: Start game from main menu
- **P**: Pause/Resume during gameplay
- **R**: Restart after game over
- **M**: Return to main menu from game over screen

### Gameplay Elements
- **🔵 Blue Circles**: Food - eat to grow and increase score
- **🟢 Green Circles**: Power-ups - temporary speed boost (5 seconds)
- **🔴 Red Squares**: Obstacles - avoid these or game over!
- **⬜ White Squares**: Snake body - do not hit yourself!

### Scoring System
- **+1 point** for each food item consumed
- **Speed increase** every time you eat
- **New obstacles** appear every 5 points
- **High score** automatically saved between sessions

## Project Structure

```
snake-game/
├── main.py           # Main game logic and state management
├── snake.py          # Snake class - movement and collision detection
├── food.py           # Food class - random placement and collision
├── scoreboard.py     # Score tracking and high score persistence
├── powerup.py        # Power-up mechanics and effects
├── obstacle.py       # Obstacle creation and positioning
├── menu_ui.py        # UI screens (menu, game over, pause)
├── data.txt          # High score storage
└── README.md         # This file
```

## Customization

### Easy Modifications

**Change Game Speed**
```python
# In main.py, modify initial game speed
self.game_speed = 0.15  # Slower start (default: 0.1)
```

**Adjust Difficulty Progression**
```python
# In increase_difficulty() method
if self.scoreboard.score % 3 == 0:  # More frequent obstacles (default: 5)
```

**Modify Colors**
```python
# In respective class files
self.color("your_color_here")
```

**Change Window Size**
```python
# In main.py __init__ method
self.screen.setup(width=800, height=800)  # Larger window (default: 600x600)
```

### Example:
- Main Screen:
![alt text](/assets/Main_Screen.png)

- Game Screen
![alt text](/assets/Game_Screen.png)

- Pause Screen
![alt text](/assets/Pause_Screen.png)

- Game Over Screen:
![alt text](/assets/Game_Over.png)