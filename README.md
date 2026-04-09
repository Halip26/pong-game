# Pong Game

Welcome to the Pong Game! This is a classic Pong game implementation using Pygame with both **Single-Player** and **Multiplayer** modes. Challenge yourself with AI or compete against a friend!

## Installation

```bash
pip install -r requirements.txt
```

## Game Modes

### 🎮 Single-Player Mode (`single_player.py`)

Play against an AI paddle with a lives system. Reach a score of 3 to win!

**Features:**

- **Lives System**: Start with 3 lives. Lose one when the ball goes out of bounds.
- **Score System**: Reach 3 points to win the game.
- **Time Limit**: Complete your objective within 10 seconds.
- **Difficulty**: Ball speed increases as you hit it.
- **HUD Display**: Real-time display of Score, Lives, and Time remaining.

**Controls:**

- `LEFT ARROW` or `A` key: Move paddle left
- `RIGHT ARROW` or `D` key: Move paddle right

**Win/Lose Conditions:**

- **Win**: Reach a score of 3 before time runs out
- **Lose**: Lose all 3 lives OR time runs out

### 👥 Multiplayer Mode (`main.py`)

Play with another player in a classic two-player Pong format.

**Controls:**

- **Player 1**: `W` to move up, `S` to move down
- **Player 2**: `UP ARROW` to move up, `DOWN ARROW` to move down

## Features

- **Background Music**: Ambient space music during gameplay
- **Score Tracking**: Real-time score display for all game modes
- **Game Timer**: Time-based gameplay to add urgency
- **Welcome Screen**: Intuitive start screen
- **Game Over Screens**: Clear feedback for wins, losses, and ties
- **Smooth Gameplay**: 60 FPS game loop for fluid motion

## How to Run

### Option 1: Single-Player Mode

```bash
python single_player.py
```

### Option 2: Multiplayer Mode

```bash
python main.py
```

### Or use the main entry point:

```bash
python main.py  # (if configured as default launcher)
```

## Code Overview

Here is a brief overview of the main parts of the game code:

- **Initialization**: Set up Pygame, the display, colors, and game variables.
- **Welcome Screen**: Displays a welcome message and waits for the player to start the game.
- **Game Loop**: The main game loop where the game logic is executed, including paddle movement, ball movement, collision detection, and score updating.
- **Game Over and Tie Screens**: Display messages when the game ends, either due to a time limit or a tie.

## Future Improvements

- **Single Player Mode**: Add an AI opponent for single-player gameplay.
- **Power-ups**: Introduce power-ups for more dynamic and interesting gameplay.
- **Customization**: Allow players to customize the game settings, such as the paddle size and ball speed.

## Acknowledgments

This game was created using the Pygame library. Special thanks to the Pygame community for their excellent documentation and tutorials.

Enjoy the game!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Developed by [Halip26](https://halip26.github.io/)
Enjoy the game!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Developed by [Halip26](https://halip26.github.io/)
