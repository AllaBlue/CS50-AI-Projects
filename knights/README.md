# Knights and Knaves Puzzle Solver

This project implements a solver for the famous **Knights and Knaves** puzzles using propositional logic. In these puzzles, characters can either be knights, who always tell the truth, or knaves, who always lie. The solver uses logical representations to infer the identity of each character based on their statements.

## Project Structure

This project contains two main files:

1. **logic.py**: Implements the propositional logic system and helper functions for evaluating logical expressions.
2. **puzzle.py**: Defines the knights and knaves puzzles, using the logic from `logic.py` to solve them.

### logic.py

The core of this file consists of logical classes used to represent symbols and logical sentences. These include:

- `Symbol`: Represents a propositional symbol (e.g., "A is a Knight").
- `Not`, `And`, `Or`, `Implication`, `Biconditional`: Logical connectives to build more complex logical sentences.
- `model_check`: Checks whether a set of logical sentences (knowledge base) entails a specific query.

### puzzle.py

This file defines four different Knights and Knaves puzzles:

- **Puzzle 0**: A says "I am both a knight and a knave."
- **Puzzle 1**: A says "We are both knaves." B says nothing.
- **Puzzle 2**: A says "We are the same kind." B says "We are of different kinds."
- **Puzzle 3**: A says either "I am a knight." or "I am a knave." B says "A said 'I am a knave'." B also says "C is a knave." C says "A is a knight."

Each puzzle is represented as a set of logical statements about the characters (A, B, and C). The `main` function prints the solution to each puzzle, showing which characters are knights and which are knaves.

## How to Run

To run the puzzles, simply execute the `puzzle.py` file:

```bash
python puzzle.py
```

This will output the solution to each of the four puzzles, identifying the roles of the characters based on the provided information.

## Example Output

For each puzzle, the program will print out whether each character is a knight or a knave. For example:

```
Puzzle 0
    A is a Knave
Puzzle 1
    B is a Knight
Puzzle 2
    A is a Knight
    B is a Knave
Puzzle 3
    C is a Knave
```

---

This project is part of the CS50AI course from Harvard University.