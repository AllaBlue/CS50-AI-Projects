# Crossword Puzzle Solver

This project implements a constraint satisfaction problem (CSP) to generate and solve crossword puzzles. It uses techniques like node consistency, arc consistency, backtracking, and the least constraining value heuristic to create valid crossword puzzles from a predefined structure and a set of words.

## Project Structure

The project consists of the following files:
- `crossword.py`: Contains the core classes to represent the crossword structure and variables.
- `generate.py`: Implements the logic to generate and solve crossword puzzles using constraint satisfaction.

### `crossword.py`
This file defines two key classes:
1. **`Variable`**: Represents a word in the crossword, defined by its starting point, direction (either across or down), and length. It also calculates the grid cells that the variable occupies.
2. **`Crossword`**: Represents the overall crossword structure, consisting of a grid and a set of possible words. It identifies variables in the crossword and computes the overlaps between them.

### `generate.py`
This file defines the `CrosswordCreator` class, which is responsible for solving the crossword using CSP techniques:
- **`solve()`**: Solves the crossword by enforcing node consistency, arc consistency (AC-3), and backtracking search.
- **`print()`**: Prints the crossword grid with the current solution.
- **`save()`**: Saves the solved crossword to an image file.
  
## How It Works
The crossword solver works by:
1. **Node consistency**: Ensuring that the length of each word matches the space available for it in the crossword.
2. **Arc consistency**: Enforcing that neighboring words overlap correctly by matching letters at the points where they intersect.
3. **Backtracking**: Attempts to assign words to variables one by one. If an assignment leads to an inconsistency, it backtracks and tries a different word.
4. **Least Constraining Value**: When assigning a word to a variable, it prioritizes words that rule out the fewest options for neighboring variables.

## Usage

1. **To generate a crossword puzzle**:
    Run the `generate.py` file by specifying a crossword structure and a word list.
    ```bash
    python generate.py data/structure.txt data/words.txt
    ```

2. **Print the crossword**:
    The crossword solution can be printed to the terminal.

3. **Save the crossword**:
    You can save the crossword solution as an image file using:
    ```python
    crossword_creator.save(assignment, "output.png")
    ```

## Example

An example of how the crossword structure looks in `data/structure.txt`:

```
_ _ █ _
█ _ █ _
_ _ _ █
```

An example of the words file (`data/words.txt`):
```
cat
bat
rat
dog
```

## Future Improvements
- Add support for more complex constraint-solving algorithms.
- Enhance the image rendering capabilities by adding more customization options.

---

This project is part of the CS50AI course from Harvard University.
