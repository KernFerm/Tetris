# Bubbles The Dev - Tetris

This is a Tetris game implemented in Python using the Pygame library. It features rotating Tetromino pieces, a scoring system, and a game-over screen.

---

## Features

- **Rotating Pieces**: Rotate Tetromino pieces with the `UP` arrow key.
- **Scoring System**: Earn points for clearing rows.
- **Smooth Gameplay**: Adjust fall speed as the game progresses for increasing difficulty.
- **Game Over Screen**: Displays "Game Over" when no valid moves are possible.

---

## Prerequisites

Make sure you have Python and Pygame installed.
- use the `install_python.bat` to install python 3.11.6 required to run this repo. 

### Install Python
Download Python from the [official Python website](https://www.python.org/) if you don’t have it installed.

### Install Pygame
Run the following command to install Pygame:
```
pip install pygame
```

## How to Run
1. Copy the provided code into a file named `tetris.py`.
2. Open a `terminal` or `command prompt`.
3. Run the following command:

```
python tetris.py
```
- use the `launcher.bat` to run the tetris.py for ease of use.

### Controls

- `Left Arrow`: Move the current piece to the left.
- `Right Arrow`: Move the current piece to the right.
- `Down Arrow`: Drop the current piece faster.
- `Up Arrow`: Rotate the current piece.

## Code Explanation

**Key Classes and Functions**

- `Tetromino Class`: Represents a Tetromino piece with its position, shape, color, and rotation.

- `Tetris Class`: Handles the game grid, current piece, game-over logic, scoring, and updating the game state.

- `valid_move Function`: Ensures the current piece's movement or rotation is within bounds and does not collide with other pieces.

- `lock_piece Function`: Locks the current piece onto the grid when it cannot move further.

- `rotate_piece Function`: Handles the rotation of Tetromino pieces, ensuring the move is valid.

- `clear_lines Function`: Clears filled rows and updates the score.

- `main Function`: The main game loop that handles events, updates the game state, and renders graphics.

## Game Logic

- **Piece Movement**: Pieces fall over time, or you can manually drop them with the Down Arrow key.

- **Line Clearing**: When a row is completely filled, it is cleared, and the score increases by 100 points per row.

- **Game Over**: The game ends when a new piece cannot spawn at the top of the grid.

---
---


# License

## ***This project is proprietary and all rights are reserved by the author.***
## ***Unauthorized copying, distribution, or modification of this project is strictly prohibited.***
## ***Unless You have written permission from the Developer or the FNBUBBLES420 ORG.***


# Credits

- Developed by **`Bubbles The Dev`**.

- Built using Pygame.
