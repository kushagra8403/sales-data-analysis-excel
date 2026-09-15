# Data Dictionary

| Field | Type | Meaning |
|---|---|---|
| order_id | string | Unique order identifier |
| order_date | date | Order date |
| region | category | Sales region |
| category | category | Product category |
| product | category | Product name |
| customer_id | string | Customer identifier |
| channel | category | Sales channel |
| quantity | integer | Units ordered |
| unit_price | numeric | Unit selling price |
| discount | numeric | Discount rate |
| sales | numeric | Order sales value |
| profit | numeric | Order profit |

**Grain:** one row per order.
