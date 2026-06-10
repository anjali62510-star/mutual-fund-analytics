import pandas as pd

performance = pd.read_csv(
    "../data/processed/07_scheme_performance_clean.csv"
)

risk = input(
    "Risk Appetite (Low/Moderate/High): "
)

if risk == "Low":
    funds = performance.nlargest(
        3,
        "sharpe_ratio"
    )

elif risk == "Moderate":
    funds = performance.nlargest(
        3,
        "return_3yr_pct"
    )

else:
    funds = performance.nlargest(
        3,
        "return_5yr_pct"
    )

print(
    funds[
        ["scheme_name",
         "sharpe_ratio"]
    ]
)
hhi = holdings.groupby(
    "sector"
)["weight_pct"].apply(
    lambda x: (x**2).sum()
)

hhi.sort_values(
    ascending=False
).head()
