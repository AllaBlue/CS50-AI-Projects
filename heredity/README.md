# Heredity

This project calculates the probabilities that individuals in a family possess a specific genetic trait based on a Bayesian network. The code models a simplified version of hereditary transmission of genes and computes the likelihood that individuals have 0, 1, or 2 copies of a particular gene. It also calculates the probability that they exhibit a trait based on their gene counts.

## Files

- `heredity.py`: The main program that implements the calculation of probabilities using Bayesian inference. It processes a CSV file containing family data and computes the joint probability of each person having certain genes and traits.

## Features

1. **Gene Probability Calculation**: 
   - Computes the probability that an individual has 0, 1, or 2 copies of a gene based on their parents' genes and the mutation rate.
   
2. **Trait Probability Calculation**: 
   - Calculates the likelihood of an individual showing a trait based on the number of genes they have.
   
3. **Bayesian Network**: 
   - A Bayesian network is used to model the probability of genes being passed from parents to children, considering possible mutations.
   
4. **Joint Probability Calculation**: 
   - Computes the joint probability for any combination of gene and trait states for a family, considering the inheritance patterns and known traits.
   
5. **Normalization**: 
   - Ensures that all probability distributions are normalized to sum to 1.

## Usage

To run the program, provide a CSV file with family data, where each person’s name, parents, and known trait status are provided.

```bash
$ python heredity.py data.csv
```

### Input CSV Format
The input CSV file should have the following columns:
- `name`: The name of the individual.
- `mother`: The individual's mother's name (can be empty if unknown).
- `father`: The individual's father's name (can be empty if unknown).
- `trait`: 1 if the individual has the trait, 0 if they do not, and blank if unknown.

### Example

```csv
name,mother,father,trait
Harry,,,"1"
James,Hermione,Ron,
Hermione,,,0
Ron,,,0
```

In this example:
- Harry has the trait.
- Hermione and Ron do not have the trait.
- James’ trait status is unknown, but his parents are Hermione and Ron.

## How It Works

1. **Load Data**: The data is loaded from the CSV file, and for each individual, their mother, father, and known trait status are recorded.
   
2. **Joint Probability Calculation**: 
   - For each combination of gene and trait states (i.e., the number of genes and whether the person has the trait), the program computes the joint probability.
   
3. **Update and Normalize**: 
   - The program updates the probabilities for each individual and normalizes them to ensure all probabilities sum to 1.
   
4. **Output**: 
   - The program prints the calculated probabilities for each person, showing the likelihood of different gene counts and whether they have the trait.

## Dependencies

This project requires no external Python libraries. It uses Python’s built-in `csv`, `itertools`, and `sys` modules.

---

This project is part of the CS50AI course from Harvard University.