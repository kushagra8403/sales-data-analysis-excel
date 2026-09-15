import pandas as pd
from pathlib import Path
df=pd.read_csv(Path(__file__).parents[1]/"data/sessions.csv")
stages=["product_view","add_to_cart","checkout","purchase"]
print("Overall funnel"); print(df[stages].sum())
print("\nStage-to-stage rates"); prev=len(df)
for s in stages:
 x=df[s].sum(); print(f"{s}: {x/prev:.1%}"); prev=x
print("\nConversion by source")
print(df.groupby("traffic_source").agg(sessions=("session_id","count"),orders=("purchase","sum"),revenue=("revenue","sum")).assign(conversion=lambda x:x.orders/x.sessions).sort_values("conversion",ascending=False).round(3))
