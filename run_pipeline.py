#!/usr/bin/env python3
"""
Pipeline orchestration script for the Titanic MLOps project.
This script automates the entire machine learning workflow.
"""

import os
import sys
import subprocess
from pathlib import Path

def run_command(script_name, description):
    """Run a Python script and handle errors."""
    original_dir = os.getcwd()
    script_path = os.path.join("src", script_name)
    print(f"\n{'='*60}")
    print(f"Running: {description}")
    print(f"Script: {script_path}")
    print(f"{'='*60}")
    
    try:
        # Change to src directory where scripts expect to run
        os.chdir("src")
        result = subprocess.run([sys.executable, script_name], check=True)
        os.chdir(original_dir)
        print(f"✓ {description} completed successfully!\n")
        return True
    except subprocess.CalledProcessError as e:
        os.chdir(original_dir)
        print(f"✗ Error running {description}")
        print(f"Error code: {e.returncode}\n")
        return False
    except Exception as e:
        os.chdir(original_dir)
        print(f"✗ Unexpected error: {e}\n")
        return False

def main():
    """Execute the complete pipeline."""
    print("\n" + "="*60)
    print("TITANIC MLOPS PIPELINE")
    print("="*60)
    
    # Define pipeline stages
    stages = [
        ("load_data.py", "Download Titanic Dataset"),
        ("preprocess.py", "Preprocess Data"),
        ("features.py", "Feature Engineering"),
        ("train.py", "Train Model"),
        ("predict.py", "Generate Predictions"),
        ("evaluate.py", "Evaluate Model"),
    ]
    
    # Run each stage
    for script, description in stages:
        if not run_command(script, description):
            print(f"\n!!! Pipeline failed at: {description} !!!")
            return 1
    
    print("\n" + "="*60)
    print("✓ PIPELINE COMPLETED SUCCESSFULLY!")
    print("="*60)
    print("\nGenerated outputs:")
    print("  - data/raw/titanic.csv (raw dataset)")
    print("  - data/processed/titanic_processed.csv (processed data)")
    print("  - features/titanic_engineered.csv (engineered features)")
    print("  - models/model.pkl (trained model)")
    print("  - results/predictions.csv (predictions)")
    print("  - results/metrics.txt (evaluation metrics)")
    print("\n")
    return 0

if __name__ == "__main__":
    sys.exit(main())
