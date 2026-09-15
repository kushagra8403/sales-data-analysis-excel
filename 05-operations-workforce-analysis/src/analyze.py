import pandas as pd
from pathlib import Path
df=pd.read_csv(Path(__file__).parents[1]/"data/workforce.csv")
print("Overall",df[["weekly_hours","absence_days_90d","tickets_or_units","sla_breaches","quality_score"]].mean().round(2))
x=df.groupby("team").agg(headcount=("employee_id","count"),avg_hours=("weekly_hours","mean"),absence=("absence_days_90d","mean"),output=("tickets_or_units","mean"),sla_breaches=("sla_breaches","mean"),quality=("quality_score","mean"));print(x.round(2))
