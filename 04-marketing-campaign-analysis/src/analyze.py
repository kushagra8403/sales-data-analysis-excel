import pandas as pd
from pathlib import Path
df=pd.read_csv(Path(__file__).parents[1]/"data/campaigns.csv")
print(df.agg(spend=("spend","sum"),revenue=("revenue","sum"),leads=("leads","sum"),conversions=("conversions","sum"),roas=("roas","mean")).round(2))
x=df.groupby("channel").agg(spend=("spend","sum"),revenue=("revenue","sum"),leads=("leads","sum"),conversions=("conversions","sum"));x["roas"]=x.revenue/x.spend;x["cac"]=x.spend/x.conversions;print(x.sort_values("roas",ascending=False).round(2))
