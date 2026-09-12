import pandas as pd
from pathlib import Path

# Find the project folder automatically
BASE_DIR = Path(__file__).resolve().parent.parent

# File locations
INPUT_FILE = BASE_DIR / "01_Data" / "student_performance.csv"
OUTPUT_FILE = BASE_DIR / "01_Data" / "student_performance_cleaned.csv"

# Load the dataset
df = pd.read_csv(INPUT_FILE)

print("First 5 rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with missing values
df = df.dropna()

# Save cleaned dataset
df.to_csv(OUTPUT_FILE, index=False)

print("\n--------------------------------")
print("Data cleaning completed successfully!")
print("--------------------------------")
print("Rows after cleaning:", len(df))
print("Cleaned file saved at:")
print(OUTPUT_FILE)