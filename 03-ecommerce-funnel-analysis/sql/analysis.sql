SELECT COUNT(*) sessions,SUM(product_view) product_views,SUM(add_to_cart) carts,SUM(checkout) checkouts,SUM(purchase) purchases,SUM(revenue) revenue FROM sessions;
SELECT traffic_source,COUNT(*) sessions,SUM(purchase) purchases,ROUND(1.0*SUM(purchase)/COUNT(*),4) conversion,ROUND(SUM(revenue),2) revenue FROM sessions GROUP BY traffic_source ORDER BY conversion DESC;
SELECT device,COUNT(*) sessions,SUM(purchase) purchases,ROUND(1.0*SUM(purchase)/COUNT(*),4) conversion FROM sessions GROUP BY device ORDER BY conversion DESC;
