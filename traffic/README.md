# Traffic Sign Recognition Project

This project implements a convolutional neural network (CNN) to recognize traffic signs from images using TensorFlow and OpenCV. The model is trained on a dataset of traffic signs, categorizing them into 43 different classes.

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)

## Overview

The goal of this project is to build a neural network that can accurately identify traffic signs in images. The main components of the project include loading and preprocessing image data, training a CNN model, and evaluating its performance on a test dataset.

## Requirements

To run this project, you need to have the following installed:

- TensorFlow
- OpenCV
- NumPy
- scikit-learn

You can install the required libraries using pip:

```bash
pip install tensorflow opencv-python numpy scikit-learn
```

## Setup

1. Prepare the dataset by organizing the traffic sign images into folders. Each folder should be named with its corresponding category label (0 to 42).
2. Place the dataset in a directory, for example, `data_directory/`.
3. Here is the link to the dataset I used: [gtsrb](https://drive.google.com/drive/folders/1G_vYR4VI8lGoJGIlJpMWa4eflCjH74QW?usp=sharing)

## Usage

To run the project, execute the following command in your terminal:

```bash
python traffic.py data_directory [model.h5]
```

- `data_directory`: The path to the directory containing your dataset.
- `[model.h5]`: (Optional) Provide a filename to save the trained model.

### Example

```bash
python traffic.py data_directory traffic_model.h5
```

This command will:
1. Load the images from the specified directory.
2. Train the model for 10 epochs.
3. Evaluate the model on a test set.
4. Save the trained model to `traffic_model.h5` if specified.