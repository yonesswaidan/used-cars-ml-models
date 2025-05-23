import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

def load_data(filepath):
    df = pd.read_csv(filepath)
    return df

def clean_data(df):
    # Drop duplicates
    df = df.drop_duplicates()

    # Drop irrelevant or mostly null columns
    df = df.drop(columns=['id', 'VIN', 'image_url', 'description'], errors='ignore')

    # Remove unrealistic prices
    df = df[(df['price'] > 1000) & (df['price'] < 100000)]

    # Drop rows with missing price
    df = df.dropna(subset=['price'])

    return df

def get_features_and_target(df):
    # Define target and features
    target = 'price'
    features = df.drop(columns=[target])
    return features, df[target]

def split_data(X, y, test_size=0.2, random_state=42):
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

def create_preprocessing_pipeline(X):
    # Identify numerical and categorical columns
    num_cols = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
    cat_cols = X.select_dtypes(include=['object']).columns.tolist()

    # Define preprocessing steps
    num_pipeline = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median'))
    ])

    cat_pipeline = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
    ])

    preprocessor = ColumnTransformer(transformers=[
        ('num', num_pipeline, num_cols),
        ('cat', cat_pipeline, cat_cols)
    ])

    return preprocessor
