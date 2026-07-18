# Sign Language Recognition using MediaPipe

A real-time sign language recognition project built with Python, OpenCV, MediaPipe, and machine learning.  
This project detects hand landmarks from a webcam feed and predicts the corresponding sign language alphabet or gesture.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Dataset Preparation](#dataset-preparation)
- [Model Information](#model-information)
- [How to Run](#how-to-run)
- [Results](#results)
- [Limitations](#limitations)
- [Future Work](#future-work)
- [Acknowledgements](#acknowledgements)

---

## Overview

This project is a sign language recognition system that uses MediaPipe to extract hand landmarks from images or webcam frames and then uses a machine learning model to classify the sign.

It is designed to:
- recognize hand signs in real time,
- help convert signs into readable labels,
- provide a simple and practical gesture recognition pipeline,
- serve as a college major project/demo.

---

## Features

- Real-time hand landmark detection using MediaPipe.
- Recognition of sign language alphabets/gestures.
- Dataset preprocessing and landmark extraction.
- CSV generation from collected image data.
- Machine learning model training.
- Webcam-based prediction.
- Easy-to-run Python scripts for testing and inference.
- Modular code structure for future improvements.

---

## Project Structure

```text
MAJOR PROJECT MCA/
├── dataset/
│   └── Indian/
├── .gitattributes
├── .gitignore
├── check_mp.py
├── collect_data.py
├── convert_dataset_to_csv.py
├── detect_landmarks.py
├── download_dataset.py
├── hand_landmarker.task
├── hand_test_new_api.py
├── indian-sign-language-isl.zip
├── isl_landmarks.csv
├── isl_model.pkl
├── main.py
├── README.md
├── requirements.txt
├── test_install.py
├── test_mp.py
├── train_model.py
└── webcam_predict.py
```

### File Description
- `dataset/Indian/`  
  Contains the collected training images arranged by class.

- `collect_data.py`  
  Used for collecting or preparing dataset samples.

- `convert_dataset_to_csv.py`  
  Extracts hand landmarks and converts the dataset into CSV format.

- `detect_landmarks.py`  
  Helper script for hand landmark detection.

- `download_dataset.py`  
  Used to download or prepare dataset resources if needed.

- `hand_landmarker.task`  
  MediaPipe hand landmark model file.

- `hand_test_new_api.py`  
  Test script for the newer MediaPipe hand API.

- `isl_landmarks.csv`  
  CSV file created from the dataset after landmark extraction.

- `isl_model.pkl`  
  Trained machine learning model file.

- `main.py`  
  Main script entry point if used.

- `test_install.py`  
  Checks whether dependencies are installed correctly.

- `test_mp.py`  
  Tests MediaPipe functionality.

- `train_model.py`  
  Trains the machine learning model using the generated CSV.

- `webcam_predict.py`  
  Runs real-time prediction from webcam input.

- `requirements.txt`  
  Lists all Python dependencies required to run the project.

---

## Requirements

- Python 3.x
- OpenCV
- MediaPipe
- NumPy
- Pandas
- scikit-learn
- Joblib
- Any other libraries used in the scripts

You can install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## Installation
## Installation Guide

Follow these steps to set up and run the project on your system.

### 1. Install Python
Make sure Python is installed on your system.  
This project was tested with Python 3.12.

You can check your Python version using:

```bash
python --version
```

If Python is not installed, download it from the official Python website and install it on your machine.

---

### 2. Open the Project Folder
Open the project folder in VS Code, Command Prompt, or Terminal.

Example:

```bash
E:\Major Project MCA
```

Make sure you are working inside the main project directory.

---

### 3. Create a Virtual Environment
It is recommended to create a virtual environment for this project.

```bash
python -m venv env
```

This creates a folder named `env` inside your project.

---

### 4. Activate the Virtual Environment

#### On Windows:
```bash
env\Scripts\activate
```

If activation is successful, your terminal will show the virtual environment name.

---

### 5. Install Required Packages
Install all dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

This will install all required libraries such as MediaPipe, OpenCV, NumPy, Pandas, scikit-learn, and Joblib.

---

### 6. Verify Installation
Run the test scripts to confirm that everything is working properly:

```bash
python test_install.py
python test_mp.py
```

If these scripts run without errors, your environment is ready.

---

### 7. Prepare the Dataset
Make sure your dataset is placed inside the `dataset/` folder.

Your dataset should be organized class-wise, for example:

```text
dataset/
└── Indian/
    ├── A/
    ├── B/
    ├── C/
    ├── D/
    └── ...
```

---

### 8. Generate the Landmark CSV
After the dataset is ready, run:

```bash
python convert_dataset_to_csv.py
```

This will create or update the `isl_landmarks.csv` file.

---

### 9. Train the Model
After generating the CSV file, train the model using:

```bash
python train_model.py
```

This will create the trained model file:

```text
isl_model.pkl
```

---

### 10. Run Real-Time Prediction
To start live sign-language prediction using your webcam, run:

```bash
python webcam_predict.py
```

A webcam window will open and start detecting the signs in real time.

---

### 11. Stop the Program
To stop the webcam program, press the key mentioned in the script, usually:

```bash
q
```

---

### 12. Add Updated Files to GitHub
After making changes, commit and push them:

```bash
git add .
git commit -m "update installation guide"
git push
```


## Dataset Preparation

The dataset is organized into labeled folders inside `dataset/Indian/`.

### Steps followed:
1. Collect images for each sign class.
2. Store the images in class-wise folders.
3. Each folder represents one label/class.
4. Run the landmark extraction script.
5. Convert the extracted landmarks into a CSV file.
6. Use the CSV file for model training.

### Example folder pattern:
```text
dataset/Indian/
├── A/
├── B/
├── C/
├── D/
├── ...
├── 1/
├── 2/
├── 3/
└── ...
```

### After dataset preparation:
Run:

```bash
python convert_dataset_to_csv.py
```

This generates `isl_landmarks.csv`, which is used for training.

---

## Model Information

## Model Version Information

- **Model file:** `isl_model.pkl`
- **Project version:** v1.0
- **Model type:** Machine learning classifier based on hand landmark features
- **Input type:** Hand landmarks extracted using MediaPipe
- **Output type:** Predicted sign/class label
- **Training file:** `isl_landmarks.csv`
- **Training script:** `train_model.py`
- **Prediction script:** `webcam_predict.py`

### Version Details
This version of the model was trained using the prepared sign language dataset and hand landmark features extracted from the dataset images.

### Notes
- This model is designed for static sign language recognition.
- The accuracy depends on dataset quality, number of samples, lighting conditions, and camera clarity.
- Future versions may include more classes, better preprocessing, and improved accuracy.

### Optional Details
- **Training date:** [add your training date]
- **Accuracy:** [add your accuracy here]
- **Model improvements:** [add any improvements in later versions]

## How to Run

### 1. Generate the CSV from dataset
If not already done:

```bash
python convert_dataset_to_csv.py
```

### 2. Train the model

```bash
python train_model.py
```

This will train the classifier and save the model as `isl_model.pkl`.

### 3. Run webcam prediction

```bash
python webcam_predict.py
```

This opens the webcam and starts predicting the sign in real time.

### 4. Stop the program
Press the key mentioned in the script, usually `q`, to quit the webcam window.

---

## Results

- The model predicts sign language gestures in real time.
- Landmark-based classification gives faster inference compared to raw image classification.
- Prediction quality depends on dataset size and camera clarity.
- Better lighting and stable hand positioning improve accuracy.

Add your own:
- accuracy score,
- confusion matrix summary,
- sample screenshots,
- test observations.

---

## Limitations

- Poor camera quality may affect landmark detection.
- Similar hand poses can be confused.
- Some alphabets may need more training samples.
- Dynamic gestures are harder than static gestures.
- Lighting and background can affect performance.

---

## Future Work

- Add more alphabets and gesture classes.
- Support additional sign languages.
- Improve the dataset with more samples.
- Add smoothing for better real-time prediction.
- Build a website or mobile app version.
- Add text-to-speech output.
- Add word/sentence prediction.

---

## Acknowledgements

- MediaPipe for hand landmark detection.
- OpenCV for image and webcam processing.
- scikit-learn for machine learning.
- Python community and open-source resources.
- Dataset contributors and project guides.

---

## Contact

If needed, add your name, email, and college details here.