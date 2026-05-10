

 
    CREATE OR REPLACE TABLE `{PROJECT_ID}.{DATASET_ID}.stg_billing` AS
    WITH dedupped AS (
      SELECT
          *,
          ROW_NUMBER() OVER(
          PARTITION BY transaction_id 
          ORDER BY CAST(transaction_date AS TIMESTAMP) DESC) as rn
      FROM `{PROJECT_ID}.{DATASET_ID}.src_billing_transactions`
    )
    SELECT 
        transaction_id, 
        customer_id, 
        COALESCE(amount, 0) as amount, 
        CAST(transaction_date AS TIMESTAMP) as transaction_date
    FROM dedupped 
    WHERE rn = 1;
    