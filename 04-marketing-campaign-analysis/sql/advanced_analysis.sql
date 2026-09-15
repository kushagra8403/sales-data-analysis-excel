-- Advanced marketing analysis: channel benchmarks and campaign ranking

WITH channel_metrics AS (
    SELECT
        channel,
        SUM(spend) AS spend,
        SUM(revenue) AS revenue,
        SUM(leads) AS leads,
        SUM(conversions) AS conversions,
        ROUND(SUM(revenue) / NULLIF(SUM(spend), 0), 2) AS roas,
        ROUND(SUM(spend) / NULLIF(SUM(conversions), 0), 2) AS cac
    FROM campaigns
    GROUP BY channel
)
SELECT *,
       RANK() OVER (ORDER BY roas DESC) AS roas_rank
FROM channel_metrics
ORDER BY roas_rank;

WITH campaign_efficiency AS (
    SELECT
        campaign_id,
        channel,
        spend,
        revenue,
        conversions,
        revenue / NULLIF(spend, 0) AS roas,
        spend / NULLIF(conversions, 0) AS cac
    FROM campaigns
)
SELECT *,
       NTILE(4) OVER (ORDER BY roas DESC) AS roas_quartile
FROM campaign_efficiency
ORDER BY roas DESC;
