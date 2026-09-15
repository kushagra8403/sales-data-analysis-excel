-- Advanced workforce analysis: team ranking and shift comparisons

WITH team_metrics AS (
    SELECT
        team,
        COUNT(*) AS headcount,
        ROUND(AVG(weekly_hours), 1) AS avg_weekly_hours,
        ROUND(AVG(absence_days_90d), 2) AS avg_absence_days,
        ROUND(AVG(tickets_or_units), 1) AS avg_output,
        ROUND(AVG(sla_breaches), 2) AS avg_sla_breaches,
        ROUND(AVG(quality_score), 2) AS avg_quality
    FROM workforce
    GROUP BY team
)
SELECT *,
       RANK() OVER (ORDER BY avg_output DESC) AS output_rank,
       RANK() OVER (ORDER BY avg_quality DESC) AS quality_rank
FROM team_metrics
ORDER BY output_rank;

WITH shift_metrics AS (
    SELECT
        shift,
        COUNT(*) AS headcount,
        ROUND(AVG(weekly_hours), 1) AS avg_hours,
        ROUND(AVG(tickets_or_units), 1) AS avg_output,
        ROUND(AVG(sla_breaches), 2) AS avg_sla_breaches
    FROM workforce
    GROUP BY shift
)
SELECT *,
       ROUND(avg_output / NULLIF(avg_hours, 0), 2) AS output_per_hour,
       LAG(avg_sla_breaches) OVER (ORDER BY avg_hours) AS prior_hours_band_sla
FROM shift_metrics;
