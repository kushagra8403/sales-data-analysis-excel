# Data Dictionary

| Field | Type | Meaning |
|---|---|---|
| employee_id | string | Unique employee identifier |
| team | category | Operational team |
| shift | category | Work shift |
| weekly_hours | numeric | Average weekly hours |
| absence_days_90d | integer | Absence days in 90 days |
| tickets_or_units | integer | Work output measure |
| sla_breaches | integer | SLA breaches attributable to the employee/team workload |
| quality_score | numeric | Quality score |

**Grain:** one row per employee.
