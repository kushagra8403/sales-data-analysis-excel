import numpy as np,pandas as pd
from pathlib import Path
r=np.random.default_rng(7); n=12000
sources=r.choice(["Organic","Paid Search","Social","Email","Referral"],n,p=[.32,.28,.16,.14,.10]); device=r.choice(["Mobile","Desktop","Tablet"],n,p=[.58,.35,.07])
view=r.random(n)<.72; cart=view&(r.random(n)<(.24+(.05*(device=="Desktop")))); checkout=cart&(r.random(n)<.58); purchase=checkout&(r.random(n)<.62)
order_value=np.round(r.lognormal(3.8,.65,n),2)*purchase
df=pd.DataFrame({"session_id":[f"S{i:06d}" for i in range(1,n+1)],"traffic_source":sources,"device":device,"product_view":view.astype(int),"add_to_cart":cart.astype(int),"checkout":checkout.astype(int),"purchase":purchase.astype(int),"revenue":order_value})
p=Path(__file__).parents[1]/"data";p.mkdir(exist_ok=True);df.to_csv(p/"sessions.csv",index=False)
