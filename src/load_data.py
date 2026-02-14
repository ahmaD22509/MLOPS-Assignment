import pandas as pd
import os

def load_data():
    """Download Titanic dataset from GitHub and save locally."""
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    df = pd.read_csv(url)
    
    os.makedirs("../data/raw", exist_ok=True)
    df.to_csv("../data/raw/titanic.csv", index=False)
    
    print("Titanic dataset downloaded and saved.")

if __name__ == "__main__":
    load_data()
