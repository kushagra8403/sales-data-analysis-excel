from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "sales_data.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA, parse_dates=["order_date"])

required = {"order_id","order_date","region","category","product","customer_id",
            "channel","quantity","unit_price","discount","sales","profit"}
missing_columns = required - set(df.columns)
if missing_columns:
    raise ValueError(f"Missing columns: {sorted(missing_columns)}")

if df["order_id"].duplicated().any():
    raise ValueError("Duplicate order IDs found")

if df[["quantity","unit_price","sales","profit"]].isna().any().any():
    raise ValueError("Unexpected missing values in core fields")

kpis = pd.DataFrame({
    "metric": ["orders","customers","sales","profit","profit_margin_pct","average_order_value"],
    "value": [len(df), df["customer_id"].nunique(), df["sales"].sum(),
              df["profit"].sum(), df["profit"].sum()/df["sales"].sum()*100,
              df["sales"].mean()]
})
kpis.to_csv(OUT/"kpis.csv", index=False)

monthly = (df.assign(month=df["order_date"].dt.to_period("M").astype(str))
             .groupby("month", as_index=False)
             .agg(sales=("sales","sum"), profit=("profit","sum"), orders=("order_id","count")))
monthly.to_csv(OUT/"monthly_performance.csv", index=False)

for name, group in [
    ("category_performance", df.groupby("category",as_index=False).agg(sales=("sales","sum"),profit=("profit","sum"),orders=("order_id","count"))),
    ("regional_performance", df.groupby("region",as_index=False).agg(sales=("sales","sum"),profit=("profit","sum"),orders=("order_id","count"))),
    ("channel_performance", df.groupby("channel",as_index=False).agg(sales=("sales","sum"),profit=("profit","sum"),orders=("order_id","count")))
]:
    group["margin_pct"] = group["profit"] / group["sales"] * 100
    group.sort_values("sales", ascending=False).to_csv(OUT/f"{name}.csv", index=False)

print("Analysis completed.")
print(kpis.to_string(index=False))
