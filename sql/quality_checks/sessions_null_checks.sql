


-- Sessions Null Checks
SELECT
    *
FROM `{PROJECT_ID}.{DATASET_ID}.src_network_sessions`
WHERE session_id IS NULL OR customer_id IS NULL;