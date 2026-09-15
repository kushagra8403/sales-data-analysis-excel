import numpy as np,pandas as pd
from pathlib import Path
r=np.random.default_rng(19); n=800
channels=r.choice(["Google Ads","Meta","LinkedIn","Email","Affiliate"],n,p=[.28,.28,.14,.16,.14]); spend=np.round(r.lognormal(7.2,.7,n),2); impressions=(spend*r.uniform(35,75,n)).astype(int); clicks=(impressions*r.uniform(.015,.09,n)).astype(int); leads=(clicks*r.uniform(.04,.25,n)).astype(int); conv=(leads*r.uniform(.04,.22,n)).astype(int); revenue=np.round(conv*r.lognormal(5.0,.35,n),2)
df=pd.DataFrame({"campaign_id":[f"CMP{i:04d}" for i in range(1,n+1)],"channel":channels,"spend":spend,"impressions":impressions,"clicks":clicks,"leads":leads,"conversions":conv,"revenue":revenue});df["roas"]=df.revenue/df.spend
p=Path(__file__).parents[1]/"data";p.mkdir(exist_ok=True);df.to_csv(p/"campaigns.csv",index=False)
