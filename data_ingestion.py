import pandas as pd
import os

data_folder = "data/raw"

csv_files = sorted(
    [f for f in os.listdir(data_folder) if f.endswith(".csv")]
)

print(f"\nFound {len(csv_files)} CSV files\n")

for file in csv_files:

    print("=" * 80)
    print(f"DATASET: {file}")

    path = os.path.join(data_folder, file)

    df = pd.read_csv(path)

    print("\nSHAPE")
    print(df.shape)

    print("\nDTYPES")
    print(df.dtypes)

    print("\nHEAD")
    print(df.head())

    print("\nMISSING VALUES")
    print(df.isnull().sum())

    print("\nDUPLICATES")
    print(df.duplicated().sum())

    print("\n")