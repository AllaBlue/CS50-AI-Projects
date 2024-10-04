# PageRank Algorithm

This project implements the PageRank algorithm, a fundamental algorithm used by search engines to rank web pages based on their link structure. The project uses two methods to calculate PageRank: by sampling and by iteration.

## Project Structure

- **`pagerank.py`**: This is the main Python script that implements the PageRank algorithm. It includes functions for:
  - Crawling through a corpus of HTML pages and extracting links.
  - Building a transition model for randomly surfing the web.
  - Calculating PageRank by random sampling.
  - Iteratively calculating PageRank until convergence.

## How It Works

1. **Crawling the Corpus**: The script takes a directory containing HTML pages as input, extracts links from each page, and creates a dictionary mapping each page to the pages it links to.
2. **Transition Model**: The transition model represents the probability distribution over the next page to visit based on the current page, considering both random jumps and following links.
3. **PageRank Calculation**:
   - **Sampling Method**: The PageRank is estimated by randomly sampling pages according to the transition model.
   - **Iterative Method**: The PageRank is iteratively calculated until the values converge, using a mathematical formula based on the damping factor and incoming links.

## Usage

To run the script, use the following command:

```bash
python pagerank.py corpus
```

Where `corpus` is a directory containing HTML files. The script will output the PageRank for each page in the corpus using both the sampling and iterative methods.

### Example

```bash
python pagerank.py example_corpus
```

Output:
```
PageRank Results from Sampling (n = 10000)
  1.html: 0.2323
  2.html: 0.3114
  3.html: 0.4563

PageRank Results from Iteration
  1.html: 0.2301
  2.html: 0.3142
  3.html: 0.4557
```

## Parameters

- `DAMPING`: The damping factor for the transition model. Default is `0.85`, meaning 85% of the time the next page is chosen from the links on the current page, and 15% of the time it's chosen randomly from all pages.
- `SAMPLES`: The number of samples used for the sampling method. Default is `10,000`.

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.