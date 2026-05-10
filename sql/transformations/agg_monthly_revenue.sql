


CREATE OR REPLACE TABLE `{PROJECT_ID}.{DATASET_ID}.agg_monthly_revenue` AS
SELECT
    customer_id,
    DATE_TRUNC(transaction_date, MONTH) AS revenue_month,
    SUM(amount) AS monthly_revenue
FROM
    `{PROJECT_ID}.{DATASET_ID}.stg_billing`
GROUP BY 1, 2;  