# Sales & Revenue Analytics

Portfolio-grade Data Analyst project using a synthetic UK retail dataset, Python, SQL and a Power BI dashboard specification.

## Business problem
Analyse sales and profitability across products, categories, regions and channels to identify revenue drivers and areas for improvement.

## Tools
- Python: pandas, NumPy, Matplotlib
- SQL: SQLite-compatible queries
- Power BI: dashboard design/specification

## Key questions
- What are total sales, profit, margin, orders and average order value?
- How does sales performance change over time?
- Which categories, regions, products and channels drive revenue?
- Which areas generate the strongest profit?
- How do discount levels relate to profitability?

## Dataset
Synthetic UK retail sales data covering January 2024 to December 2025. It contains 3,000 orders across six regions, three categories and three sales channels.

## Key results
- Total sales: **£1,877,247.21**
- Total profit: **£322,599.79**
- Overall profit margin: **17.18%**
- Orders: **3,000**
- Average order value: **£625.75**

## Project structure
```text
01-sales-revenue-analysis/
├── README.md
├── sales_data.csv
├── requirements.txt
├── sql/
│   └── analysis.sql
├── src/
│   └── analyze.py
├── dashboard/
│   └── dashboard_spec.md
├── reports/
│   └── findings.md
└── visuals/
    ├── monthly_sales.png
    ├── category_sales.png
    └── region_profit.png
```

## Run locally
```bash
pip install -r requirements.txt
python src/analyze.py
```

The analysis script validates the data and exports summary tables to `outputs/`.

## Portfolio note
The dataset is synthetic and exists for portfolio demonstration. The findings must not be interpreted as real company performance.
