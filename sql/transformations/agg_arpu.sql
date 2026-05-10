
--NULLIF(count, 0) is used to avoid the division by zero error.
-- If a user has 0 active months, the result is NULL, which is safer than failing the entire pipeline


CREATE OR REPLACE TABLE `{PROJECT_ID}.{DATASET_ID}.agg_arpu` AS
SELECT
    customer_id,
    SUM(amount) / NULLIF(COUNT(DISTINCT DATE_TRUNC(transaction_date, MONTH)), 0) AS arpu
FROM
    `{PROJECT_ID}.{DATASET_ID}.stg_billing`
GROUP BY 1;