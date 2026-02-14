import pandas as pd
import joblib
import os
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def evaluate():
    """Evaluate the trained model and save metrics."""
    df = pd.read_csv("../features/titanic_engineered.csv")
    X = df.drop(columns=['Survived'])
    y = df['Survived']
    
    model = joblib.load("../models/model.pkl")
    predictions = model.predict(X)
    
    # Calculate metrics
    accuracy = accuracy_score(y, predictions)
    precision = precision_score(y, predictions)
    recall = recall_score(y, predictions)
    f1 = f1_score(y, predictions)
    
    os.makedirs("../results", exist_ok=True)
    with open("../results/metrics.txt", "w") as f:
        f.write(f"Model Evaluation Metrics\n")
        f.write(f"=======================\n")
        f.write(f"Accuracy:  {accuracy:.4f}\n")
        f.write(f"Precision: {precision:.4f}\n")
        f.write(f"Recall:    {recall:.4f}\n")
        f.write(f"F1 Score:  {f1:.4f}\n")
        
    print("Evaluation complete. Metrics saved to results/metrics.txt")
    print(f"Accuracy:  {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")
    print(f"F1 Score:  {f1:.4f}")

if __name__ == "__main__":
    evaluate()