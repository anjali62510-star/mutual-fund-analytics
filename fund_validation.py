import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

print("="*60)
print("FUND MASTER EXPLORATION")
print("="*60)

print("Fund Houses:", fund_master["fund_house"].nunique())
print("Categories:", fund_master["category"].unique())
print("Sub Categories:", fund_master["sub_category"].unique())
print("Risk Categories:", fund_master["risk_category"].unique())

master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = master_codes - nav_codes

print("\nMissing AMFI Codes:", len(missing_codes))

print("\nFund Master Missing Values")
print(fund_master.isnull().sum())

print("\nNAV History Missing Values")
print(nav_history.isnull().sum())

print("\nFund Master Duplicates:", fund_master.duplicated().sum())
print("NAV History Duplicates:", nav_history.duplicated().sum())