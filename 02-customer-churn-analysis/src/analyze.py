import pandas as pd
from pathlib import Path
p=Path(__file__).parents[1]; df=pd.read_csv(p/"data/customers.csv")
churn=df.churned.mean(); mrr=df.loc[df.churned.eq(0),"monthly_charge"].sum(); risk=df.loc[df.churned.eq(1),"monthly_charge"].sum()
print({"customers":len(df),"churn_rate":round(churn,4),"active_mrr":round(mrr,2),"monthly_revenue_at_risk":round(risk,2)})
print("\nChurn by plan")
print(df.groupby("plan").agg(customers=("customer_id","count"),churn_rate=("churned","mean"),revenue_at_risk=("monthly_charge",lambda s:s[df.loc[s.index,"churned"].eq(1)].sum())).round(3))
print("\nChurn by tenure band")
df["tenure_band"]=pd.cut(df.tenure_months,[0,6,12,24,60],labels=["0-6","7-12","13-24","25+"])
print(df.groupby("tenure_band",observed=False).churned.mean().round(3))
