import psycopg2
import os



def run_quality_checks():
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        user=os.environ.get('PG_USER'),
        password=os.environ.get('PG_PASSWORD'),
        host=os.environ.get('PG_HOST'),
        port=os.environ.get('PG_PORT'),
        database=os.environ.get('PG_DATABASE')
    )
    cursor = conn.cursor()
    
    
    # Null checks
    cursor.execute("SELECT COUNT(*) FROM src_billing_transactions WHERE customer_id IS NULL;")
    null_count = cursor.fetchone()[0]
    print(f"Null Customer IDs in Billing: {null_count}")
    
    # Duplicate checks
    cursor.execute(
        """
        SELECT transaction_id, COUNT(*)
        FROM src_billing_transactions
        GROUP BY transaction_id
        HAVING COUNT(*) > 1
        LIMIT 5;
        """
    )
    duplicates = cursor.fetchall()
    print(f"Duplicate Transactions in Billing: {len(duplicates)}")
    for transaction_id, count in duplicates:
        print(f"  - Transaction ID: {transaction_id}, Count: {count}")
        
    cursor.close()
    conn.close()
    