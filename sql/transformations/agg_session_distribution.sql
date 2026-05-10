


CREATE OR REPLACE TABLE `{PROJECT_ID}.{DATASET_ID}.agg_session_distribution` AS
WITH session_buckets AS (
    SELECT
        customer_id,
        CASE
            WHEN session_duration_sec < 60 THEN 'short'
            WHEN session_duration_sec BETWEEN 60 AND 299 THEN 'medium'
            ELSE 'long'
        END AS bucket
    FROM
        `{PROJECT_ID}.{DATASET_ID}.stg_sessions`
)
SELECT
    customer_id,
    COUNTIF(bucket = 'short') AS short_sessions,
    COUNTIF(bucket = 'medium') AS medium_sessions,
    COUNTIF(bucket = 'long') AS long_sessions
FROM
    session_buckets
GROUP BY 1;