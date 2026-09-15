from pathlib import Path
import numpy as np
import pandas as pd

SEED = 42
N = 3000
ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / 'data'
DATA_DIR.mkdir(exist_ok=True)

rng = np.random.default_rng(SEED)
dates = pd.date_range('2024-01-01', '2025-12-31', freq='D')
regions = ['London','Birmingham','Manchester','Leeds','Bristol','Glasgow']
region_p = [0.22,0.18,0.16,0.13,0.11,0.20]
categories = ['Technology','Office Supplies','Home']
cat_p = [0.42,0.32,0.26]
products = {
    'Technology':['Laptop','Monitor','Keyboard','Headphones','Smartphone'],
    'Office Supplies':['Notebook','Desk Chair','Printer','Desk Lamp','Backpack'],
    'Home':['Coffee Maker','Vacuum Cleaner','Desk','Bookshelf','Air Purifier']
}
price_ranges = {
    'Laptop':(650,950),'Monitor':(180,550),'Keyboard':(35,180),'Headphones':(45,350),'Smartphone':(250,900),
    'Notebook':(4,25),'Desk Chair':(45,260),'Printer':(70,320),'Desk Lamp':(15,90),'Backpack':(30,180),
    'Coffee Maker':(60,260),'Vacuum Cleaner':(100,500),'Desk':(100,500),'Bookshelf':(80,350),'Air Purifier':(90,450)
}
margin = {'Technology':0.19,'Office Supplies':0.22,'Home':0.20}
channels = ['Online','Store','Corporate']
channel_p = [0.50,0.35,0.15]
rows=[]
for i in range(1,N+1):
    category = rng.choice(categories, p=cat_p)
    product = rng.choice(products[category])
    qty = int(rng.integers(1,6))
    price = round(float(rng.uniform(*price_ranges[product])),2)
    discount = float(rng.choice([0,.05,.10,.15,.20], p=[.35,.20,.25,.15,.05]))
    gross = qty * price
    sales = round(gross * (1-discount),2)
    effective_margin = margin[category] - discount*0.35 + float(rng.normal(0,0.01))
    profit = round(max(sales * effective_margin, sales*0.03),2)
    rows.append([i, rng.choice(dates), rng.choice(regions,p=region_p), category, product,
                 f'C{int(rng.integers(1001,1451))}', rng.choice(channels,p=channel_p), qty, price,
                 discount, sales, profit])

cols=['order_id','order_date','region','category','product','customer_id','channel','quantity','unit_price','discount','sales','profit']
df=pd.DataFrame(rows, columns=cols)
df.to_csv(DATA_DIR/'sales_data.csv', index=False)
print(f'Generated {len(df):,} orders at {DATA_DIR / "sales_data.csv"}')
