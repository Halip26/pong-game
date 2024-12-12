# Pong Game

Welcome to the Pong Game! This is a simple implementation of the classic Pong game using Pygame. Enjoy playing against a friend and see who can score the most points before the time runs out!

## Install

```bash
pip install -r .\requirements.txt
```

## Features

- **Music**: Background music that loops during the game.
- **Score Tracking**: Keep track of the scores for both players.
- **Game Timer**: The game ends after 2 minutes, and the winner is determined.
- **Tie Condition**: If the scores are tied when the time runs out, a "TIE" message is displayed.
- **Welcome Screen**: A welcome screen that prompts the player to start the game.

## Controls

- **Player 1**: Use `W` to move up and `S` to move down.
- **Player 2**: Use the `Up` arrow key to move up and the `Down` arrow key to move down.

## How to Run

1. **Install Pygame**: Make sure you have Python and Pygame installed. You can install Pygame using the following command:

    ```sh
    pip install pygame
    ```

2. **Run the Game**: Save the game code to a file, e.g., `pong_game.py`, and run it using Python:

    ```sh
    python pong_game.py
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
