

    CREATE OR REPLACE TABLE `{PROJECT_ID}.{DATASET_ID}.stg_sessions` AS 
    SELECT
        session_id, 
        customer_id,
        CAST(start_time AS TIMESTAMP) as start_ts,
        CAST(end_time AS TIMESTAMP) as end_ts,
        COALESCE(data_used_mb, 0) as data_used_mb,
        
        CASE
            WHEN CAST(end_time AS TIMESTAMP) > CAST(start_time AS TIMESTAMP) 
            THEN TIMESTAMP_DIFF(CAST(end_time AS TIMESTAMP), CAST(start_time AS TIMESTAMP), SECOND)
            ELSE 0
        END AS session_duration_sec
    FROM `{PROJECT_ID}.{DATASET_ID}.src_network_sessions`;
