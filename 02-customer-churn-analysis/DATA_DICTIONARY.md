# Data Dictionary

| Field | Type | Meaning |
|---|---|---|
| customer_id | string | Unique customer identifier |
| plan | category | Subscription plan |
| acquisition_channel | category | Customer acquisition source |
| tenure_months | integer | Months since acquisition |
| monthly_charge | numeric | Monthly recurring charge |
| monthly_usage_hours | numeric | Monthly product usage |
| support_contacts_90d | integer | Support contacts in the last 90 days |
| satisfaction_score | numeric | Customer satisfaction score |
| churned | integer | 1 = churned, 0 = retained |

**Grain:** one row per customer.
