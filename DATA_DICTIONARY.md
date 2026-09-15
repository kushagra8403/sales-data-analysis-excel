# Portfolio Data Dictionary

All datasets in this repository are synthetic and reproducible. The dictionary below summarises the main analytical fields used across the six projects.

## 01 — Sales & Revenue

| Field | Meaning |
|---|---|
| order_id | Unique order identifier |
| order_date | Order date |
| region | UK sales region |
| category | Product category |
| product | Product name |
| customer_id | Customer identifier |
| channel | Sales channel |
| quantity | Units ordered |
| unit_price | Price per unit |
| discount | Applied discount |
| sales | Order revenue |
| profit | Order profit |

## 02 — Customer Churn

| Field | Meaning |
|---|---|
| customer_id | Customer identifier |
| plan | Subscription plan |
| acquisition_channel | Customer acquisition source |
| tenure_months | Customer tenure |
| monthly_charge | Recurring monthly charge |
| monthly_usage_hours | Monthly usage |
| support_contacts_90d | Support contacts in prior 90 days |
| satisfaction_score | Customer satisfaction measure |
| churned | Binary churn outcome |

## 03 — E-commerce Funnel

| Field | Meaning |
|---|---|
| session_id | Session identifier |
| source | Acquisition source |
| device | Device category |
| product_view | Product-view event flag |
| add_to_cart | Cart event flag |
| checkout | Checkout event flag |
| purchase | Purchase event flag |
| revenue | Session revenue |

## 04 — Marketing Campaigns

| Field | Meaning |
|---|---|
| campaign_id | Campaign identifier |
| channel | Marketing channel |
| spend | Campaign spend |
| impressions | Ad impressions |
| clicks | Clicks |
| leads | Leads generated |
| conversions | Converted leads |
| revenue | Attributed revenue |
| roas | Revenue divided by spend |

## 05 — Workforce

| Field | Meaning |
|---|---|
| employee_id | Employee identifier |
| team | Operational team |
| shift | Work shift |
| weekly_hours | Weekly scheduled hours |
| absence_days_90d | Absence days in prior 90 days |
| tickets_or_units | Operational output |
| sla_breaches | SLA breach count |
| quality_score | Quality performance measure |

## 06 — Executive KPI Model

| Field | Meaning |
|---|---|
| month | Reporting month |
| revenue | Monthly revenue |
| profit | Monthly profit |
| active_customers | Active customer count |
| orders | Monthly orders |
| marketing_spend | Monthly marketing spend |
| sla_breach_rate | SLA breach rate |
| profit_margin | Profit divided by revenue |
| aov | Average order value |
| roas | Revenue divided by marketing spend |

## Methodology note

Metrics are designed for portfolio demonstration rather than real-world reporting. Any business decision using production data would require agreed metric definitions, source-system reconciliation and validation with stakeholders.
