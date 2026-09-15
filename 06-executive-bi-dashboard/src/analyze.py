import pandas as pd
from pathlib import Path
df=pd.read_csv(Path(__file__).parents[1]/"data/executive_kpis.csv");df.month=pd.to_datetime(df.month)
print(df[["revenue","profit","active_customers","orders","marketing_spend","sla_breach_rate","profit_margin","aov","roas"]].sum(numeric_only=True).round(2))
print("\nLatest month"); print(df.tail(1).T)
print("\nTrend change"); print(((df.tail(1).iloc[0]-df.iloc[0])/df.iloc[0]).round(3))
