


SELECT 
    *
FROM
    `datatel.dw_user_analytics.dw_user_analytics`
WHERE
    total_data_used_mb > 10000
    AND total_revenue < 500;