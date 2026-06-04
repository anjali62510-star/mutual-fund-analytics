from sqlalchemy import create_engine
import pandas as pd
from pathlib import Path

# Create database folder if it doesn't exist
Path("data/db").mkdir(parents=True, exist_ok=True)

# Create SQLite database
engine = create_engine(
    "sqlite:///data/db/bluestock_mf.db"
)

processed = Path("data/processed")

print("Loading cleaned CSVs into SQLite...\n")

for file in processed.glob("*.csv"):

    table_name = file.stem.replace("_clean", "")

    df = pd.read_csv(file)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(
        f"Loaded {table_name} "
        f"({len(df)} rows)"
    )

print("\nDatabase loading complete!")