
-- Duplicate checks
SELECT
    transaction_id,
    COUNT(*) as count
FROM `{PROJECT_ID}.{DATASET_ID}.src_billing_transactions`
GROUP BY 1 
HAVING count > 1;


