# Tic-Tac-Toe with AI

This project implements the classic Tic-Tac-Toe game with an AI opponent that uses the Minimax algorithm to determine the best moves. You can play against the AI as either X or O. The game features a graphical interface built using `pygame`.

## Project Structure

- **`tictactoe.py`**: Contains the logic for the Tic-Tac-Toe game, including game state management, Minimax AI, and utility functions.
- **`runner.py`**: Runs the graphical version of the game using `pygame`. Allows users to play against the AI with a user-friendly interface.

## How It Works

1. **Minimax Algorithm**: The AI calculates the optimal move by simulating all possible outcomes of the game. 
   - If it's the AI's turn, it maximizes its own score (assuming it's X).
   - If it's the player's turn, it minimizes the AI's score.
2. **Game State Management**: Functions such as `initial_state`, `player`, `actions`, `result`, and `terminal` manage the current state of the board and determine the game's progress.
3. **Graphical Interface**: The game uses `pygame` to display the board and handle user interactions, including choosing a player, clicking on tiles, and resetting the game.

## How to Play

1. **Run the Game**: Use the following command to start the game:
   ```bash
   python runner.py
   ```

2. **Choosing a Player**: When the game starts, you'll be asked to choose whether to play as X or O.

3. **Making Moves**: 
   - Click on an empty tile to place your mark (X or O).
   - The AI will make its move automatically after yours.
   - The game continues until there's a winner or the board is full (a tie).

4. **End of Game**: Once the game is over, you can click "Play Again" to start a new game.

### Game Controls

- **Left Click**: Place your mark (X or O) on an empty tile.
- **Play Again**: After a game ends, click the "Play Again" button to start a new game.

## Requirements

- `pygame` library

To install `pygame`, run:
```bash
pip install pygame
```

## Code Overview

### `tictactoe.py`

- **`initial_state()`**: Initializes the 3x3 board with empty cells.
- **`player(board)`**: Determines which player's turn it is (X or O).
- **`actions(board)`**: Returns the set of possible actions (empty cells).
- **`result(board, action)`**: Returns the new board state after a player makes a move.
- **`winner(board)`**: Returns the winner of the game (X, O, or None).
- **`terminal(board)`**: Returns whether the game is over (True or False).
- **`utility(board)`**: Returns the game score (1 for X win, -1 for O win, 0 for tie).
- **`minimax(board)`**: Determines the optimal action using the Minimax algorithm.

### `runner.py`

This script uses `pygame` to create the graphical interface for the game:
- **Player Selection**: Allows the user to choose whether to play as X or O.
- **Game Loop**: Handles user input, displays the current board, and determines when the game is over.
- **AI Move**: The AI uses the `minimax` function from `tictactoe.py` to make its move.

## Example

When you run the game, you'll see a window like this:

```
---------------------
|     |     |     |
|  X  |     |  O  |
|     |     |     |
---------------------
|     |     |     |
|     |  X  |     |
|     |     |     |
---------------------
|     |     |     |
|     |     |     |
|  O  |     |  X  |
---------------------
```

The AI will make its move automatically after yours. The game ends when there's a winner or the board is full.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to enhance the game or improve the AI.