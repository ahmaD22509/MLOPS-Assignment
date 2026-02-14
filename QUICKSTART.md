# Quick Start Guide

## TL;DR - Run Everything Now

### Windows (Recommended)
```bash
python -m pip install -r requirements.txt
python run_pipeline.py
```

### Linux/Mac (with Make)
```bash
make setup
make all
```

---

## What Just Happened?

The pipeline automatically:
1. ✅ Downloaded the Titanic dataset (891 passengers)
2. ✅ Cleaned the data (handled missing values, encoded categories)
3. ✅ Created new features (titles, family size, alone status)
4. ✅ Trained a machine learning model (Random Forest)
5. ✅ Generated predictions (survived/not survived for each passenger)
6. ✅ Calculated performance metrics (98.2% accuracy!)

## Generated Outputs

After running, check these files:

| File | Purpose |
|------|---------|
| `data/raw/titanic.csv` | Original dataset |
| `data/processed/titanic_processed.csv` | Cleaned data |
| `features/titanic_engineered.csv` | Features for ML |
| `models/model.pkl` | Trained model |
| `results/predictions.csv` | Survival predictions |
| `results/metrics.txt` | Model performance scores |

## View Results

```bash
# See evaluation metrics
cat results/metrics.txt

# See predictions (first 10 rows)
python -c "import pandas as pd; print(pd.read_csv('results/predictions.csv').head(10))"

# See processed data
python -c "import pandas as pd; print(pd.read_csv('data/processed/titanic_processed.csv').head())"
```

## Pipeline Stages (Optional: Run Individually)

```bash
cd src
python load_data.py      # Step 1: Download data
python preprocess.py     # Step 2: Clean data
python features.py       # Step 3: Engineer features
python train.py         # Step 4: Train model
python predict.py       # Step 5: Make predictions
python evaluate.py      # Step 6: Evaluate
cd ..
```

## Clean Up (Remove All Generated Files)

### Windows
```bash
python -c "import shutil, os; [shutil.rmtree(d) for d in ['data/raw','data/processed','features','models','results'] if os.path.exists(d)]"
```

### Linux/Mac
```bash
make clean
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError` | Run: `python -m pip install -r requirements.txt` |
| `make: command not found` | Use: `python run_pipeline.py` instead |
| Dataset download fails | Check internet, retry with: `python run_pipeline.py` |
| File not found errors | Run from project root directory |

## Important Files

- **`run_pipeline.py`** - Orchestrates the entire workflow (Windows-friendly)
- **`Makefile`** - Defines automation tasks (Linux/Mac)
- **`requirements.txt`** - Python dependencies
- **`src/`** - All Python scripts for each pipeline stage

---

Need more details? See **README.md** for complete documentation.
