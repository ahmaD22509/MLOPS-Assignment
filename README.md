# MLOps Assignment: Titanic Dataset Pipeline

## Overview
This project implements an end-to-end machine learning pipeline for the Titanic dataset using automated workflows with Makefile (for Unix-like systems) and Python orchestration scripts (for Windows/cross-platform).

## Project Objective
Build a reproducible, automated ML pipeline that:
- Downloads the Titanic dataset automatically
- Preprocesses and cleans data
- Performs feature engineering
- Trains a Random Forest classifier
- Generates predictions
- Evaluates model performance

## Project Structure
```
titanic_mlops/
├── Makefile                          # Automation targets for Unix-like systems
├── requirements.txt                  # Python dependencies
├── run_pipeline.py                   # Python-based pipeline orchestrator (Windows-compatible)
├── data/
│   ├── raw/                         # Downloaded raw dataset
│   └── processed/                   # Preprocessed data
├── src/
│   ├── load_data.py                # Download Titanic dataset
│   ├── preprocess.py               # Data cleaning and preprocessing
│   ├── features.py                 # Feature engineering
│   ├── train.py                    # Model training (Random Forest)
│   ├── predict.py                  # Generate predictions
│   └── evaluate.py                 # Model evaluation
├── features/                        # Engineered features storage
├── models/                          # Trained model storage
└── results/                         # Predictions and metrics
```

## Installation

### Step 1: Install Dependencies

**Using pip:**
```bash
pip install -r requirements.txt
```

**Or using Python module:**
```bash
python -m pip install -r requirements.txt
```

### Step 2: Verify Installation
```bash
python -c "import pandas, numpy, sklearn, joblib, matplotlib; print('All dependencies installed successfully!')"
```

## Running the Pipeline

### Option 1: Python Script (Recommended for Windows)
```bash
python run_pipeline.py
```

This will execute all pipeline stages in sequence:
1. Download Dataset
2. Preprocess Data
3. Feature Engineering
4. Train Model
5. Generate Predictions
6. Evaluate Model

### Option 2: Using Make (Linux/Mac or with GNU Make installed)
```bash
# Install dependencies
make setup

# Run entire pipeline
make all

# Or run individual stages:
make download-data    # Download dataset
make preprocess       # Preprocess data
make features         # Feature engineering
make train           # Train model
make predict         # Generate predictions
make evaluate        # Evaluate model
```

### Option 3: Manual Execution (for debugging)
```bash
cd src
python load_data.py      # Download dataset
python preprocess.py     # Preprocess data
python features.py       # Feature engineering
python train.py         # Train model
python predict.py       # Generate predictions
python evaluate.py      # Evaluate model
cd ..
```

## Pipeline Stages

### 1. Data Download (`load_data.py`)
- Downloads Titanic dataset from GitHub
- Saves to `data/raw/titanic.csv`

### 2. Preprocessing (`preprocess.py`)
- Handles missing values (Age, Embarked)
- Encodes categorical variables (Sex, Embarked)
- Selects relevant features
- Saves to `data/processed/titanic_processed.csv`

### 3. Feature Engineering (`features.py`)
- Extracts titles from passenger names
- Creates family size feature
- Creates "IsAlone" feature
- Saves engineered features to `features/titanic_engineered.csv`

### 4. Model Training (`train.py`)
- Trains Random Forest classifier (100 estimators)
- Saves model to `models/model.pkl`

### 5. Prediction (`predict.py`)
- Generates predictions using trained model
- Saves predictions to `results/predictions.csv`

### 6. Evaluation (`evaluate.py`)
- Calculates performance metrics:
  - Accuracy
  - Precision
  - Recall
  - F1-Score
- Saves metrics to `results/metrics.txt`

## Output Files

After running the pipeline, the following files are generated:

- **`data/raw/titanic.csv`** - Original dataset (891 passengers)
- **`data/processed/titanic_processed.csv`** - Cleaned and preprocessed data
- **`features/titanic_engineered.csv`** - Data with engineered features
- **`models/model.pkl`** - Trained Random Forest model
- **`results/predictions.csv`** - Model predictions for each passenger
- **`results/metrics.txt`** - Evaluation metrics

## Model Performance

The Random Forest classifier achieves excellent performance:
- **Accuracy**: ~98.2% - Proportion of correct predictions
- **Precision**: ~98.8% - Accuracy of positive predictions
- **Recall**: ~96.5% - Coverage of actual positive cases
- **F1-Score**: ~97.6% - Harmonic mean of precision and recall

## Dependencies

- **pandas** (3.0.0+) - Data manipulation
- **numpy** (2.4.0+) - Numerical computing
- **scikit-learn** (1.8.0+) - Machine learning
- **joblib** (1.5.0+) - Model serialization
- **matplotlib** (3.10.0+) - Visualization

## Cleaning Up

To remove all generated artifacts:

**Using Python script:**
```bash
python -c "
import shutil
import os
dirs = ['data/raw', 'data/processed', 'features', 'models', 'results']
for d in dirs:
    if os.path.exists(d):
        shutil.rmtree(d)
"
```

**Using Make:**
```bash
make clean
```

**Manual cleanup:**
```bash
rm -rf data/raw/*
rm -rf data/processed/*
rm -rf features/*
rm -rf models/*
rm -rf results/*
```

## Technical Details

### Technologies Used
- Python 3.14+
- GNU Make (optional, for Unix-like systems)
- scikit-learn (Random Forest)
- pandas (Data manipulation)

### Dataset
- **Source**: Titanic Survival Dataset (Kaggle)
- **Samples**: 891 passengers
- **Target**: Survived (0 or 1)
- **Features**: Passenger class, sex, age, family members, fare, embarkation port

### Algorithm
- **Model**: Random Forest Classifier
- **Reason**: Handles both numerical and categorical data, provides feature importance
- **Hyperparameters**: 100 estimators, random state 42

## Troubleshooting

### Issue: "No such file or directory" errors
**Solution**: Ensure you're running scripts from the project root directory.

### Issue: Module not found errors
**Solution**: Install dependencies: `python -m pip install -r requirements.txt`

### Issue: Make command not found (Windows)
**Solution**: Use `python run_pipeline.py` instead, or install GNU Make via:
- Chocolatey: `choco install make`
- WSL: Use Windows Subsystem for Linux
- Git Bash: Comes with GNU Make

### Issue: Network timeout downloading dataset
**Solution**: 
- Check internet connection
- Verify GitHub is accessible
- Retry the pipeline: `python run_pipeline.py`

## Academic Integrity
This assignment must be completed individually. Code sharing or plagiarism violates academic integrity policies.

## License
Educational assignment - use only for learning purposes.

---

**Created**: February 2026  
**Python Version**: 3.14+  
**Last Updated**: February 14, 2026
