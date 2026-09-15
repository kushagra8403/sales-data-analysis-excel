-- Advanced executive KPI analysis: rolling metrics and period-over-period change

WITH monthly AS (
    SELECT
        month,
        revenue,
        profit,
        active_customers,
        orders,
        marketing_spend,
        sla_breach_rate,
        profit_margin,
        aov,
        roas
    FROM executive_kpis
)
SELECT *,
       ROUND(AVG(revenue) OVER (
           ORDER BY month
           ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
       ), 2) AS revenue_3m_avg,
       ROUND(AVG(profit_margin) OVER (
           ORDER BY month
           ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
       ), 4) AS margin_3m_avg,
       LAG(revenue) OVER (ORDER BY month) AS prior_month_revenue,
       ROUND(100.0 * (revenue - LAG(revenue) OVER (ORDER BY month))
             / NULLIF(LAG(revenue) OVER (ORDER BY month), 0), 2) AS revenue_mom_pct
FROM monthly
ORDER BY month;

WITH ranked_months AS (
    SELECT *,
           RANK() OVER (ORDER BY revenue DESC) AS revenue_rank,
           RANK() OVER (ORDER BY roas DESC) AS roas_rank
    FROM executive_kpis
)
SELECT *
FROM ranked_months
ORDER BY revenue_rank;
