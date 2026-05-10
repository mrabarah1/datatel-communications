

SELECT
    customer_name,
    total_revenue,
    CASE
        WHEN total_revenue > 5000000 THEN 'High Value'
        WHEN total_revenue > 1000000 THEN 'Mid Value'
        ELSE 'Low Value'
    END AS customer_segment
FROM
    `datatel.dw_user_analytics.dw_user_analytics`
ORDER BY total_revenue DESC
LIMIT 10;