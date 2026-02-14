import pandas as pd
import joblib
import os

def predict():
    """Generate predictions using the trained model."""
    df = pd.read_csv("../features/titanic_engineered.csv")
    X = df.drop(columns=['Survived'])
    
    model = joblib.load("../models/model.pkl")
    predictions = model.predict(X)
    
    # Create results dataframe
    results_df = pd.DataFrame({
        'PassengerId': range(len(predictions)),
        'Survived_Prediction': predictions
    })
    
    os.makedirs("../results", exist_ok=True)
    results_df.to_csv("../results/predictions.csv", index=False)
    print("Predictions generated and saved to results/predictions.csv")

if __name__ == "__main__":
    predict()
