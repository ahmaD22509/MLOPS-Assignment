import pandas as pd
import os

def preprocess():
    """Preprocess Titanic dataset by handling missing values and encoding categorical variables."""
    df = pd.read_csv("../data/raw/titanic.csv")
    
    # Fill missing values
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
    
    # Encode categorical variables
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
    df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})
    
    # Select features and target
    features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked', 'Survived']
    df = df[features]
    
    os.makedirs("../data/processed", exist_ok=True)
    df.to_csv("../data/processed/titanic_processed.csv", index=False)
    print("Data preprocessed and saved.")

if __name__ == "__main__":
    preprocess()