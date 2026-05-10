


SELECT
    customer_name,
    total_sessions,
    total_revenue,
    CASE
        WHEN total_sessions < 5 AND total_revenue < 1000 THEN 'High Risk'
        ELSE 'Active'
    END AS churn_risk
FROM
    `datatel.dw_user_analytics.dw_user_analytics`;