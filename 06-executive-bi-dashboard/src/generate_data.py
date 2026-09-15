import numpy as np,pandas as pd
from pathlib import Path
r=np.random.default_rng(55); months=pd.date_range("2025-01-01",periods=24,freq="MS"); n=len(months)
df=pd.DataFrame({"month":months,"revenue":np.round(r.normal(210000,18000,n),2),"profit":np.round(r.normal(36000,5000,n),2),"active_customers":r.integers(2600,3400,n),"orders":r.integers(900,1400,n),"marketing_spend":np.round(r.normal(28000,4500,n),2),"sla_breach_rate":np.round(r.uniform(.035,.075,n),4)})
df["profit_margin"]=df.profit/df.revenue;df["aov"]=df.revenue/df.orders;df["roas"]=df.revenue/df.marketing_spend
p=Path(__file__).parents[1]/"data";p.mkdir(exist_ok=True);df.to_csv(p/"executive_kpis.csv",index=False)
