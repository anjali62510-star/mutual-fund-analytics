import pandas as pd
from pathlib import Path

RAW = Path("data/raw")
PROCESSED = Path("data/processed")

PROCESSED.mkdir(exist_ok=True)

print("Starting ETL...")
fund = pd.read_csv(RAW / "01_fund_master.csv")

fund = fund.drop_duplicates()

fund["launch_date"] = pd.to_datetime(
    fund["launch_date"],
    errors="coerce"
)

fund.to_csv(
    PROCESSED / "01_fund_master_clean.csv",
    index=False
)

print("fund_master cleaned")

nav = pd.read_csv(RAW / "02_nav_history.csv")

nav["date"] = pd.to_datetime(
    nav["date"],
    errors="coerce"
)

nav = nav.sort_values(
    ["amfi_code", "date"]
)

nav = nav.drop_duplicates()

nav = nav[nav["nav"] > 0]

nav["nav"] = (
    nav.groupby("amfi_code")["nav"]
    .ffill()
)

nav.to_csv(
    PROCESSED / "02_nav_history_clean.csv",
    index=False
)

print("nav_history cleaned")

tx = pd.read_csv(
    RAW / "08_investor_transactions.csv"
)

tx["transaction_date"] = pd.to_datetime(
    tx["transaction_date"],
    errors="coerce"
)

tx["transaction_type"] = (
    tx["transaction_type"]
    .str.upper()
    .str.strip()
)

tx["kyc_status"] = (
    tx["kyc_status"]
    .str.upper()
    .str.strip()
)

tx = tx[tx["amount_inr"] > 0]

tx.to_csv(
    PROCESSED / "08_investor_transactions_clean.csv",
    index=False
)

print("transactions cleaned")

perf = pd.read_csv(
    RAW / "07_scheme_performance.csv"
)

cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct"
]

for col in cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

anomalies = perf[
    (perf["expense_ratio_pct"] < 0.1) |
    (perf["expense_ratio_pct"] > 2.5)
]

anomalies.to_csv(
    PROCESSED / "expense_ratio_anomalies.csv",
    index=False
)

perf.to_csv(
    PROCESSED / "07_scheme_performance_clean.csv",
    index=False
)

print("scheme_performance cleaned")

files = [
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files:
    df = pd.read_csv(RAW / file)

    df.to_csv(
        PROCESSED / file.replace(".csv", "_clean.csv"),
        index=False
    )

print("All datasets processed")