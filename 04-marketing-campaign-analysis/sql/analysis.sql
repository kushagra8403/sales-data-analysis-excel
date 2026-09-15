SELECT channel,ROUND(SUM(spend),2) spend,ROUND(SUM(revenue),2) revenue,SUM(leads) leads,SUM(conversions) conversions,ROUND(SUM(revenue)/SUM(spend),2) roas,ROUND(SUM(spend)/NULLIF(SUM(conversions),0),2) cac FROM campaigns GROUP BY channel ORDER BY roas DESC;
SELECT campaign_id,channel,spend,revenue,ROUND(revenue/spend,2) roas FROM campaigns ORDER BY roas DESC LIMIT 10;
