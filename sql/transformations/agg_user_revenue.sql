

CREATE OR REPLACE TABLE `{PROJECT_ID}.{DATASET_ID}.agg_user_revenue` AS
SELECT
    customer_id,
    SUM(amount) AS total_revenue,
    COUNT(transaction_id) AS total_transactions
FROM
    `{PROJECT_ID}.{DATASET_ID}.stg_billing`
GROUP BY 1;

