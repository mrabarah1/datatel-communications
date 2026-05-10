

-- Billing Null Checks 
SELECT
    *
FROM `{PROJECT_ID}.{DATASET_ID}.src_billing_transactions`
WHERE transaction_id IS NULL OR customer_id IS NULL;


