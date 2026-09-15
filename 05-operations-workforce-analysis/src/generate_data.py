import numpy as np,pandas as pd
from pathlib import Path
r=np.random.default_rng(31); n=1800
teams=r.choice(["Customer Service","Warehouse","Operations","Technical Support"],n); shifts=r.choice(["Morning","Afternoon","Evening"],n); hours=np.round(r.normal(37,5,n).clip(15,55),1); absence=np.round(r.exponential(1.5,n),1); tickets=(hours*r.normal(3.2,0.45,n)-absence*2).clip(5).astype(int); breaches=(tickets*r.uniform(.03,.15,n)).astype(int); quality=np.clip(r.normal(92,4,n)-absence*.5,70,100).round(1)
df=pd.DataFrame({"employee_id":[f"E{i:05d}" for i in range(1,n+1)],"team":teams,"shift":shifts,"weekly_hours":hours,"absence_days_90d":absence,"tickets_or_units":tickets,"sla_breaches":breaches,"quality_score":quality});p=Path(__file__).parents[1]/"data";p.mkdir(exist_ok=True);df.to_csv(p/"workforce.csv",index=False)
