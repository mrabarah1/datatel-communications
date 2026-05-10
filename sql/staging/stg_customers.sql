


    CREATE OR REPLACE TABLE `{PROJECT_ID}.{DATASET_ID}.stg_customers` AS
    SELECT 
        customer_id,
        INITCAP(name) as customer_name,
        LOWER(email) as email,
        COALESCE(country, 'Nigeria') as country,
        CAST(created_at AS TIMESTAMP) as created_at
    FROM `{PROJECT_ID}.{DATASET_ID}.src_customers`;
