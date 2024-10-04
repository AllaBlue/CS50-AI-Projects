# Nim Game with AI

This project implements the classic game of Nim with an AI that uses Q-learning to improve its performance over time. Players can compete against an AI that trains itself by playing thousands of games to learn optimal strategies.

## Project Structure

The project consists of the following files:

- `nim.py`: Contains the logic for the game of Nim and an AI that uses Q-learning for training and playing the game.
- `play.py`: Trains the AI by playing 10,000 games against itself and then starts a game where a human player can play against the AI.

## Game Rules

Nim is a simple two-player game where players take turns removing objects from piles. Each player must remove at least one object from one of the piles, and the player who removes the last object loses the game.

### Game Features

- **AI Player**: The AI learns by playing games against itself using Q-learning.
- **Human Player**: You can play against the trained AI.
- **Q-learning**: The AI learns from its mistakes and successes by updating Q-values associated with states and actions.

## How to Play

### Gameplay

- When the game starts, the current state of the piles is displayed.
- The human player will be prompted to choose a pile and the number of objects to remove from that pile.
- The AI will make its move after the human player.
- The game continues until all piles are empty, at which point the winner is declared.

### Example of a Game Session

```
Playing training game 1
...
Playing training game 10000
Done training

Piles:
Pile 0: 1
Pile 1: 3
Pile 2: 5
Pile 3: 7

Your Turn
Choose Pile: 2
Choose Count: 3

AI's Turn
AI chose to take 2 from pile 3.

Piles:
Pile 0: 1
Pile 1: 3
Pile 2: 2
Pile 3: 5
```

## AI Training

The AI is trained using Q-learning. It plays a large number of games against itself and updates its knowledge based on the outcomes of those games. The AI starts with no knowledge of the game and improves its strategy as it plays more games.

- **Q-learning Parameters**:
  - `alpha`: Learning rate, controls how much new information overrides old information.
  - `epsilon`: Exploration rate, determines how often the AI chooses a random move instead of the best known move.

### Training Function

You can adjust the number of training games in `play.py`:

```python
ai = train(10000)
```

Change `10000` to a different number to train the AI with more or fewer games.

---

This project is part of the CS50AI course from Harvard University.