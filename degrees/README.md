# Degrees of Separation

This project implements a search algorithm to find the shortest path between two actors or actresses using the "degrees of separation" concept. It calculates how closely two people are connected in the film industry, based on the movies they have starred in together.

## Project Structure

The project consists of the following files:

1. `degrees.py`: The main script that loads the data, prompts the user for input, and finds the shortest connection (degrees of separation) between two actors/actresses using a breadth-first search (BFS) algorithm.
2. `util.py`: Contains helper classes for the search algorithm, including `Node`, `StackFrontier`, and `QueueFrontier`.

## How It Works

### Data

The project uses three CSV files (stored in the `large` or `small` directories):
- `people.csv`: Contains information about actors and actresses (ID, name, birth year).
- `movies.csv`: Contains information about movies (ID, title, year).
- `stars.csv`: Links actors/actresses to movies they starred in.

### Search Algorithm

The search for the shortest path between two people is performed using the **breadth-first search (BFS)** algorithm, implemented with the `QueueFrontier` class from `util.py`. The algorithm works by:
1. Initializing the search with the source actor/actress.
2. Exploring the neighbors (co-stars) of each person.
3. Finding a path to the target actor/actress with the fewest degrees of separation (fewest movie co-star links).

### Example

When prompted, users input the names of two actors/actresses. The program will calculate and display the shortest path of movies connecting the two, if any exists.

#### Example Output:
```
Name: Tom Hanks
Name: Kevin Bacon
Loading data...
Data loaded.
2 degrees of separation.
1: Tom Hanks and Meg Ryan starred in Sleepless in Seattle
2: Meg Ryan and Kevin Bacon starred in In the Cut
```

### Usage

1. Place the `degrees.py` and `util.py` files in the project directory.
2. Download the `small` or `large` dataset containing the CSV files (`people.csv`, `movies.csv`, and `stars.csv`). Here is a link of small and large data I used: [small_large](https://drive.google.com/drive/folders/1idt6xXCc7lhkdGqOrJ3D3LNrPJS6FmW2?usp=sharing)
3. Run the program:
   ```bash
   python degrees.py [directory]
   ```
   If no directory is provided, the program will default to using the `small` dataset.

   Example:
   ```bash
   python degrees.py large
   ```

4. Enter the names of the actors/actresses when prompted.

### Notes

- If the input names refer to multiple people (e.g., multiple actors with the same name), the user will be asked to select the correct one by ID.
- If no connection is found between the two actors, the program will output `Not connected.`.

---

This project is part of the CS50AI course from Harvard University.