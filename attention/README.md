# Attention Visualization with BERT

This project demonstrates how to use a pre-trained BERT model to visualize self-attention mechanisms. The model predicts missing words in sentences and generates visual diagrams of attention heads and layers to illustrate how words in the sentence "pay attention" to each other.

## Project Files

- **mask.py**: The main script that handles tokenizing input, predicting missing words, and generating visual attention diagrams.
- **analysis.md**: A detailed analysis of attention patterns in different layers and heads of the BERT model.

## Features

1. **Masked Language Model Predictions**: 
   - The script uses the pre-trained `bert-base-uncased` model to predict the most likely words to replace the `[MASK]` token in a given sentence.
   - It generates `K` predictions and prints out the sentences with each prediction.

2. **Attention Visualization**:
   - After generating predictions, the script produces visualizations of the self-attention scores.
   - For each attention layer and head, the script generates a grid-based diagram where the shade of each cell represents the attention score between tokens.
   - The diagrams are saved as images, named by their corresponding layer and head numbers.

## How to Use

1. **Input**: Provide a sentence with a `[MASK]` token when prompted by the script. Example:
   ```
   Text: We turned down a narrow lane and passed through a small [MASK].
   ```

2. **Output**: The script will generate:
   - A list of predicted words for the `[MASK]` token.
   - Diagrams that visualize the attention patterns for each attention head and layer.

## Example

Given the input:
```
The turtle slowly moved across the [MASK].
```

The model might predict:
```
The turtle slowly moved across the road.
The turtle slowly moved across the ground.
The turtle slowly moved across the field.
```

The script will also generate attention diagrams like this:

- **Layer 1, Head 3**: Words focus heavily on their preceding words.
- **Layer 1, Head 11**: Words focus on their following words.

## Running the Project

1. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the script:
   ```bash
   python mask.py
   ```

## Analysis

For a detailed analysis of the attention patterns across different layers and heads, refer to the `analysis.md` file.

---

This project is part of the CS50AI course from Harvard University.