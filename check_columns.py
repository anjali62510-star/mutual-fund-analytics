import pandas as pd
import os

for file in sorted(os.listdir("data/raw")):
    if file.endswith(".csv"):
        df = pd.read_csv(f"data/raw/{file}")
        print("\n" + "="*80)
        print(file)
        print(df.columns.tolist())