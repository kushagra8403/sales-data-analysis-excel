import numpy as np, pandas as pd
from pathlib import Path
rng=np.random.default_rng(42); n=2500
plans=rng.choice(["Basic","Standard","Premium"],n,p=[.35,.45,.20])
channels=rng.choice(["Organic","Paid Search","Referral","Partner"],n,p=[.35,.25,.2,.2])
tenure=rng.integers(1,61,n); charges=np.round(np.where(plans=="Basic",25,np.where(plans=="Standard",45,75))*rng.normal(1,0.08,n),2)
usage=np.round(rng.gamma(3,8,n),1); support=rng.poisson(1.2,n); satisfaction=np.clip(np.round(rng.normal(7.1,1.6,n),1),1,10)
logit=-2.4-0.018*tenure+0.055*support-0.23*(satisfaction-5)+0.018*(usage<12)+0.25*(plans=="Basic")
p=1/(1+np.exp(-logit)); churn=rng.random(n)<p
df=pd.DataFrame({"customer_id":[f"C{i:05d}" for i in range(1,n+1)],"plan":plans,"acquisition_channel":channels,"tenure_months":tenure,"monthly_charge":charges,"monthly_usage_hours":usage,"support_contacts_90d":support,"satisfaction_score":satisfaction,"churned":churn.astype(int)})
out=Path(__file__).parents[1]/"data"; out.mkdir(exist_ok=True); df.to_csv(out/"customers.csv",index=False)
print(f"Created {len(df):,} customers")
