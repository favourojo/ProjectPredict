import pandas as pd 
import glob
import os

chunk_jobs = [
    ("C://Users//favou//Documents//Machine Learning//Project//ML_Project//data//raw//chunks//Donation Chunks", 
     "C://Users//favou//Documents//Machine Learning//Project//ML_Project//data//processed//cleaned_projects.csv"),
    ("C://Users//favou//Documents//Machine Learning//Project//ML_Project//data//raw//chunks//Outcome Chunks", 
     "C://Users//favou//Documents//Machine Learning//Project//ML_Project//data//processed//cleaned_outcomes.csv"),
    ("C://Users//favou//Documents//Machine Learning//Project//ML_Project//data//raw//chunks//Project Chunks", 
     "C://Users//favou//Documents//Machine Learning//Project//ML_Project//data//processed//cleaned_donations.csv")
]

def clean_data(df):
    df.columns = df.columns.str.strip().str.lower()

    num_cols = df.select_dtypes(include='number').columns
    for col in num_cols:
        if df[col].isnull().any():
            df[col] = df[col].fillna(df[col].median())

    cat_cols = df.select_dtypes(include='object').columns
    for col in cat_cols:
        if df[col].isnull().any() and not df[col].mode().empty:
            df[col] = df[col].fillna(df[col].mode()[0])
    
    return df

# Process each set of chunks
for folder_path, output_file in chunk_jobs:
    file_paths = sorted(glob.glob(os.path.join(folder_path, "*.csv")))
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Remove output file if it exists (for reruns)
    if os.path.exists(output_file):
        os.remove(output_file)

    for i, file_path in enumerate(file_paths):
        df = pd.read_csv(file_path)
        cleaned_df = clean_data(df)

        # Append to CSV, write header only for the first chunk
        cleaned_df.to_csv(output_file, mode='a', index=False, header=(i == 0))
