import pandas as pd
import joblib
import os
from sklearn.ensemble import RandomForestClassifier

def train():
    """Train a Random Forest classifier on engineered features."""
    df = pd.read_csv("../features/titanic_engineered.csv")
    X = df.drop(columns=['Survived'])
    y = df['Survived']
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    os.makedirs("../models", exist_ok=True)
    joblib.dump(model, "../models/model.pkl")
    print("Model trained and saved to models/model.pkl")

if __name__ == "__main__":
    train()