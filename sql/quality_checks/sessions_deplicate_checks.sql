


-- Sessions Duplicate Checks
SELECT
    session_id,
    COUNT(*) as count
FROM `{PROJECT_ID}.{DATASET_ID}.src_network_sessions`
GROUP BY 1
HAVING count > 1;