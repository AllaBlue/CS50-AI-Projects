# Minesweeper AI Project

This is a Python implementation of the classic **Minesweeper** game, along with an AI agent that attempts to solve the board using logical reasoning.

## Project Overview

The project contains two key components:

1. **Minesweeper Game**: A Python representation of the Minesweeper game, which randomly generates a grid of mines and allows a player to interact with the game.
2. **Minesweeper AI**: An AI that uses logical inferences to determine safe cells and mines. The AI uses the number of nearby mines for each revealed cell and keeps track of safe moves and potential mines through logical deduction.

### File Structure

- `minesweeper.py`: Contains the logic for both the game and the AI.
- `runner.py`: The Pygame interface where players can play Minesweeper and test the AI.

## Minesweeper Game

The game board is generated as a grid, with randomly placed mines. Players can click cells to reveal if they are safe or contain a mine. The player wins by flagging all mines without detonating any.

### Key Methods

- `is_mine(cell)`: Returns whether the cell contains a mine.
- `nearby_mines(cell)`: Returns the number of mines near a given cell.
- `won()`: Checks if the player has flagged all mines correctly.

## Minesweeper AI

The AI makes safe moves using its knowledge base. It tracks its own moves, flagged mines, and inferred safe cells. The AI can:

- Make safe moves based on previous knowledge.
- Infer new safe cells or mines through logical deduction.
- If no safe moves are available, the AI will make a random move from the remaining unclicked cells.

### AI Methods

- `mark_mine(cell)`: Marks a cell as a mine.
- `mark_safe(cell)`: Marks a cell as safe.
- `add_knowledge(cell, count)`: Adds knowledge to the AI based on the number of mines surrounding a revealed cell.
- `make_safe_move()`: Returns a known safe cell for the next move.
- `make_random_move()`: Chooses a random move if no safe moves are known.

## How to Run

1. Install Pygame using the following command:
   ```bash
   pip install pygame
   ```
2. Clone or download this repository.
3. Run the game using the `runner.py` file:
   ```bash
   python runner.py
   ```

### Gameplay Instructions

- **Left-click** on a cell to reveal it.
- **Right-click** on a cell to flag it as a mine.
- Use the **AI Move** button to let the AI make a safe move.
- Use the **Reset** button to start a new game.

## Future Improvements

- Implementing different difficulty levels (varying the number of mines and grid size).
- Optimizing the AI's logic for better performance on larger grids.
- Enhancing the GUI for a more interactive and user-friendly experience.

Enjoy playing and testing the AI's abilities in solving Minesweeper!

---

This project is part of the CS50AI course from Harvard University.

