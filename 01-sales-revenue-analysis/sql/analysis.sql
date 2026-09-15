-- Sales & Revenue Analytics
-- SQLite-compatible SQL

SELECT COUNT(*) AS orders,
       ROUND(SUM(sales),2) AS total_sales,
       ROUND(SUM(profit),2) AS total_profit,
       ROUND(SUM(profit)/NULLIF(SUM(sales),0)*100,2) AS profit_margin_pct,
       ROUND(AVG(sales),2) AS average_order_value
FROM sales_data;

SELECT strftime('%Y-%m', order_date) AS month,
       ROUND(SUM(sales),2) AS sales,
       ROUND(SUM(profit),2) AS profit,
       COUNT(*) AS orders
FROM sales_data
GROUP BY 1 ORDER BY 1;

SELECT category, ROUND(SUM(sales),2) AS sales,
       ROUND(SUM(profit),2) AS profit,
       ROUND(SUM(profit)/NULLIF(SUM(sales),0)*100,2) AS margin_pct
FROM sales_data GROUP BY category ORDER BY sales DESC;

SELECT region, ROUND(SUM(sales),2) AS sales,
       ROUND(SUM(profit),2) AS profit, COUNT(*) AS orders,
       ROUND(SUM(profit)/NULLIF(SUM(sales),0)*100,2) AS margin_pct
FROM sales_data GROUP BY region ORDER BY profit DESC;

SELECT product, ROUND(SUM(sales),2) AS sales,
       ROUND(SUM(profit),2) AS profit, SUM(quantity) AS units
FROM sales_data GROUP BY product ORDER BY sales DESC LIMIT 10;

SELECT channel, ROUND(SUM(sales),2) AS sales,
       ROUND(SUM(profit),2) AS profit,
       ROUND(SUM(profit)/NULLIF(SUM(sales),0)*100,2) AS margin_pct
FROM sales_data GROUP BY channel ORDER BY sales DESC;

SELECT CASE
         WHEN discount=0 THEN '0%'
         WHEN discount<=0.05 THEN '1-5%'
         WHEN discount<=0.10 THEN '6-10%'
         WHEN discount<=0.15 THEN '11-15%'
         ELSE '16-20%'
       END AS discount_band,
       COUNT(*) AS orders, ROUND(SUM(sales),2) AS sales,
       ROUND(SUM(profit),2) AS profit,
       ROUND(SUM(profit)/NULLIF(SUM(sales),0)*100,2) AS margin_pct
FROM sales_data
GROUP BY discount_band ORDER BY MIN(discount);
