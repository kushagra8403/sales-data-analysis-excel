-- Advanced churn analysis: CTEs, window functions and risk segmentation

WITH plan_metrics AS (
    SELECT
        plan,
        COUNT(*) AS customers,
        SUM(churned) AS churned_customers,
        ROUND(100.0 * SUM(churned) / COUNT(*), 2) AS churn_rate,
        ROUND(SUM(CASE WHEN churned = 1 THEN monthly_charge ELSE 0 END), 2) AS monthly_revenue_at_risk
    FROM customers
    GROUP BY plan
), ranked_plans AS (
    SELECT *,
           RANK() OVER (ORDER BY churn_rate DESC) AS churn_rate_rank
    FROM plan_metrics
)
SELECT *
FROM ranked_plans
ORDER BY churn_rate_rank;

WITH tenure_bands AS (
    SELECT
        CASE
            WHEN tenure_months < 6 THEN '0-5'
            WHEN tenure_months < 12 THEN '6-11'
            WHEN tenure_months < 24 THEN '12-23'
            ELSE '24+'
        END AS tenure_band,
        COUNT(*) AS customers,
        ROUND(AVG(satisfaction_score), 2) AS avg_satisfaction,
        ROUND(100.0 * AVG(churned), 2) AS churn_rate
    FROM customers
    GROUP BY tenure_band
)
SELECT *,
       LAG(churn_rate) OVER (ORDER BY tenure_band) AS prior_band_churn_rate
FROM tenure_bands;
