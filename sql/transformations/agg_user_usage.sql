




CREATE OR REPLACE TABLE `{PROJECT_ID}.{DATASET_ID}.agg_user_usage` AS
SELECT
    customer_id,
    SUM(data_used_mb) AS total_data_used_mb,
    AVG(session_duration_sec) AS avg_session_duration_sec
FROM
    `{PROJECT_ID}.{DATASET_ID}.stg_usage`
GROUP BY 1;  