# Shopping Prediction Model

This project uses a machine learning model to predict whether a user will generate revenue on an e-commerce platform based on various factors like browsing behavior, session information, and user attributes. The model is built using the k-nearest neighbors (KNN) algorithm.

## Project Structure

- **`shopping.py`**: This script contains the main code to:
  - Load and preprocess shopping data from a CSV file.
  - Train a KNN model to classify user sessions as generating revenue or not.
  - Evaluate the model’s performance in terms of sensitivity and specificity.

## How It Works

1. **Data Loading**: The `load_data` function reads data from a CSV file and converts it into features (evidence) and labels (revenue). Each session's evidence includes various attributes like administrative data, product information, bounce rates, and more.
   
2. **Model Training**: The `train_model` function trains a KNN classifier (k=1) using the training data.
   
3. **Prediction and Evaluation**: The model is evaluated using the test data, calculating sensitivity (true positive rate) and specificity (true negative rate) using the `evaluate` function.

## Data Format

Link for the dataset I used: [shoppig.csv](https://drive.google.com/drive/folders/1XDHcxGnB0j6a1UMjPD-jqJTEYRthm0BV?usp=sharing)

The data file should be in CSV format and include the following columns (in order):
1. `Administrative` (integer)
2. `Administrative_Duration` (float)
3. `Informational` (integer)
4. `Informational_Duration` (float)
5. `ProductRelated` (integer)
6. `ProductRelated_Duration` (float)
7. `BounceRates` (float)
8. `ExitRates` (float)
9. `PageValues` (float)
10. `SpecialDay` (float)
11. `Month` (string, e.g., "Jan", "Feb", etc.)
12. `OperatingSystems` (integer)
13. `Browser` (integer)
14. `Region` (integer)
15. `TrafficType` (integer)
16. `VisitorType` (string, "Returning_Visitor" or other)
17. `Weekend` (string, "TRUE" or "FALSE")
18. `Revenue` (string, "TRUE" or "FALSE")

## Usage

To run the program, use the following command:

```bash
python shopping.py data.csv
```

Where `data.csv` is the path to your dataset file.

### Example

```bash
python shopping.py shopping_data.csv
```

The script will:
- Load the data from the specified file.
- Split the data into training and testing sets (60% training, 40% testing).
- Train a KNN model.
- Predict whether each session in the test set will generate revenue.
- Output the number of correct and incorrect predictions, along with the sensitivity and specificity of the model.

### Output Example:

```
Correct: 1200
Incorrect: 400
True Positive Rate: 85.00%
True Negative Rate: 70.00%
```

## Model Details

- **Algorithm**: k-nearest neighbors (k=1)
- **Test Size**: 40% of the data is used for testing, 60% for training.

### Evaluation Metrics:
- **Sensitivity (True Positive Rate)**: Proportion of actual positive cases (Revenue = 1) that were correctly predicted by the model.
- **Specificity (True Negative Rate)**: Proportion of actual negative cases (Revenue = 0) that were correctly predicted by the model.

## Requirements
- `scikit-learn`

You can install the required packages using pip:

```bash
pip install scikit-learn
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.