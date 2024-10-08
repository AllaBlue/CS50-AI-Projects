import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping/shopping.py shopping/data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """

    evidence = []
    labels = []
    
    # Dictionary that maps months names to appropriate number between 0 and 11
    months = {
        "Jan": 0,
        "Feb": 1,
        "Mar": 2,
        "Apr": 3,
        "May": 4,
        "Jun": 5,
        "June": 5,
        "Jul": 6,
        "Aug": 7,
        "Sep": 8,
        "Oct": 9,
        "Nov": 10,
        "Dec": 11
    }

    # reading csv file into lists
    with open(file=filename, mode="r") as file:
        csvreader = csv.reader(file)
        # skipping headers
        header = next(csvreader)
        for row in csvreader:
            # creating a parsed row
            parsed_row = []
            for i, r in enumerate(row):
                # converting strings to integers
                if i in [0, 2, 4, 11, 12, 13, 14]:
                    parsed_row.append(int(r))
                elif i in [1, 3, 5, 6, 7, 8, 9]:
                    # converting strings to floats
                    parsed_row.append(float(r))
                elif i == 10:
                    # parse the month name to number
                    parsed_row.append(months[r])
                elif i == 15:
                    # parse column for the returning visitor status
                    if r == "Returning_Visitor":
                        parsed_row.append(int(1))
                    else:
                        parsed_row.append(int(0))
                elif i == 16:
                    # parse column that has TRUE and FALSE values into integers
                    if r == "TRUE":
                        parsed_row.append(int(1))
                    elif r == "FALSE":
                        parsed_row.append(int(0))
                # parse labels
                elif i == 17:
                    if r == "TRUE":
                        labels.append(int(1))
                    elif r == "FALSE":
                        labels.append(int(0))
            
            evidence.append(parsed_row)
    
    return (evidence, labels)


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(X=evidence, y=labels)
    return model


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    
    true_positive_count = 0
    all_positive = 0
    true_negative_count = 0
    all_negative = 0

    # comparing each prediction with corresponding label
    for label, prediction in zip(labels, predictions):
        # if model predicted that the output is true correctly, then it is true positive
        if label == 1 and prediction == 1:
            true_positive_count += 1
        
        # if model predicted correctly that the output is false, then it is true negative
        elif label == 0 and prediction == 0:
            true_negative_count += 1
        
        # counting all real false values and true values in the dataset
        if label == 0:
            all_negative += 1
        elif label == 1:
            all_positive += 1
    
    # getting the proportion
    sensitivity = true_positive_count/all_positive
    specificity = true_negative_count/all_negative

    return (sensitivity, specificity)


if __name__ == "__main__":
    main()