-- Advanced funnel analysis: CTEs and source ranking

WITH source_funnel AS (
    SELECT
        source,
        COUNT(*) AS sessions,
        SUM(product_view) AS product_views,
        SUM(add_to_cart) AS carts,
        SUM(checkout) AS checkouts,
        SUM(purchase) AS purchases,
        SUM(revenue) AS revenue
    FROM sessions
    GROUP BY source
), rates AS (
    SELECT *,
           ROUND(100.0 * purchases / NULLIF(sessions, 0), 2) AS conversion_rate
    FROM source_funnel
)
SELECT *,
       RANK() OVER (ORDER BY conversion_rate DESC) AS conversion_rank
FROM rates
ORDER BY conversion_rank;

WITH device_monthly AS (
    SELECT
        device,
        strftime('%Y-%m', session_date) AS month,
        COUNT(*) AS sessions,
        SUM(purchase) AS purchases
    FROM sessions
    GROUP BY device, month
)
SELECT *,
       ROUND(100.0 * purchases / NULLIF(sessions, 0), 2) AS conversion_rate,
       LAG(purchases) OVER (PARTITION BY device ORDER BY month) AS prior_month_purchases
FROM device_monthly
ORDER BY device, month;
