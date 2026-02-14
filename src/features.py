import pandas as pd
import os
import re

def extract_title(name):
    """Extract title from passenger name."""
    title_search = re.search(r' ([A-Za-z]+)\.', name)
    if title_search:
        return title_search.group(1)
    return 'Unknown'

def engineer_features():
    """Perform feature engineering on preprocessed data."""
    df = pd.read_csv("../data/processed/titanic_processed.csv")
    
    # Reload raw data to extract titles and create new features
    raw_df = pd.read_csv("../data/raw/titanic.csv")
    
    # Extract title from names
    df['Title'] = raw_df['Name'].apply(extract_title)
    
    # Group rare titles
    title_value_counts = df['Title'].value_counts()
    rare_titles = title_value_counts[title_value_counts < 10].index
    df['Title'] = df['Title'].replace(rare_titles, 'Rare')
    
    # Encode title
    title_mapping = {'Mr': 0, 'Mrs': 1, 'Miss': 2, 'Master': 3, 'Rare': 4, 'Unknown': 5}
    df['Title'] = df['Title'].map(title_mapping).fillna(0)
    
    # Create Family Size feature
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    
    # Create IsAlone feature
    df['IsAlone'] = (df['FamilySize'] == 1).astype(int)
    
    # Drop original family-related columns if needed
    # df = df.drop(columns=['SibSp', 'Parch'])
    
    os.makedirs("../features", exist_ok=True)
    df.to_csv("../features/titanic_engineered.csv", index=False)
    print("Feature engineering complete. Features saved.")

if __name__ == "__main__":
    engineer_features()
