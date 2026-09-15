-- SQLite-compatible churn analysis
SELECT COUNT(*) customers, AVG(churned) churn_rate, SUM(CASE WHEN churned=1 THEN monthly_charge ELSE 0 END) revenue_at_risk FROM customers;
SELECT plan, COUNT(*) customers, ROUND(AVG(churned),3) churn_rate, ROUND(SUM(CASE WHEN churned=1 THEN monthly_charge ELSE 0 END),2) revenue_at_risk FROM customers GROUP BY plan ORDER BY revenue_at_risk DESC;
SELECT acquisition_channel, ROUND(AVG(churned),3) churn_rate, COUNT(*) customers FROM customers GROUP BY acquisition_channel ORDER BY churn_rate DESC;
SELECT CASE WHEN tenure_months<=6 THEN '0-6' WHEN tenure_months<=12 THEN '7-12' WHEN tenure_months<=24 THEN '13-24' ELSE '25+' END tenure_band, ROUND(AVG(churned),3) churn_rate FROM customers GROUP BY tenure_band ORDER BY churn_rate DESC;
