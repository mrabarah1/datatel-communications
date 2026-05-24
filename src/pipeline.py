from google.cloud import bigquery
import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import pyarrow 


load_dotenv()

# PostgreSQL Configurations
user = os.getenv("PG_USER")
password = os.getenv("PG_PASSWORD")
host = os.getenv("PG_HOST")
port = os.getenv("PG_PORT")
db = os.getenv("PG_DATABASE")

PG_URL = f"postgresql://{user}:{password}@{host}:{port}/{db}"
engine = create_engine(PG_URL)

# BigQuery Configurations
PROJECT_ID = os.getenv("GCP_PROJECT_ID")
DATASET_ID = os.getenv("BQ_DATASET_ID")
BQ_CLIENT = bigquery.Client(project=PROJECT_ID)

def execute_sql_file(file_path, client):
    """Executes a local SQL file on BigQuery."""
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return
    
    with open(file_path, 'r') as file:
        sql = file.read()
        
    p_id = os.getenv("GCP_PROJECT_ID")
    d_id = os.getenv("BQ_DATASET_ID")
        
    sql = sql.replace("{PROJECT_ID}", str(p_id))
    sql = sql.replace("{DATASET_ID}", str(d_id))
    
    print(f"DEBUG: First 50 chars of processed SQL: {sql[:50]}...")
    
    try:
        query_job = client.query(sql)
        query_job.result()  # Wait for the query to complete
        print(f"Executed Successfully: {file_path}")
    except Exception as e:
        print(f"Error executing {file_path}: {e}")
        raise e




def run_pipeline():
    # Extract Data from Postgres, Using pandas to read and upload to BigQuery
    
    # Load raw data from Postgres to BigQuery
    tables = [
        "src_customers",
        "src_billing_transactions",
        "src_network_sessions"
    ]
    
    #Use context manager to ensure connection is closed after operations
    with engine.connect() as conn:
        
        #loops through my postgres table and pulls the data into pandas df
        for table in tables:
            # Extract validated data out of PostgreSQL using pandas
            df = pd.read_sql(f"SELECT * FROM {table}", conn)
            
            # Streams and loads the data into BigQuery
            destination_table = f"{PROJECT_ID}.{DATASET_ID}.{table}"
            job_config = bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE", autodetect=True)
            job = BQ_CLIENT.load_table_from_dataframe(df, destination_table, job_config=job_config)
            job.result()  # Wait for the job to complete
            print(f"Loaded {table} to BigQuery successfully.")
    
    # staging and transformation steps will be executed directly in BigQuery using SQL files
    print("Starting Stage 2: Staging...")
    # List of staging SQL files to be executed in order
    staging_tasks = [
       "sql/staging/stg_billing.sql",
       "sql/staging/stg_sessions.sql",
       "sql/staging/stg_customers.sql"
    ]
    # Executes each staging SQL file sequentially on BigQuery
    for task in staging_tasks:
        execute_sql_file(task, BQ_CLIENT)
   
    
    #  TRANSFORMATIONS
    print("Starting Stage 3: Transformations...")
    # List of transformation SQL files to be executed in order
    transform_tasks = [
        "sql/transformations/agg_user_revenue.sql",
        "sql/transformations/agg_user_usage.sql",
        "sql/transformations/agg_monthly_revenue.sql",
        "sql/transformations/agg_arpu.sql",
        "sql/transformations/session_buckets.sql",
        "sql/transformations/agg_session_distribution.sql"
    ]
    # Executes each transformation SQL file sequentially on BigQuery
    for task in transform_tasks:
        execute_sql_file(task, BQ_CLIENT)

    # WAREHOUSE
    print("Starting Stage 4: Warehouse...")
    # Executes the warehouse SQL file to create the final analytics tables in BigQuery
    execute_sql_file("sql/warehouse/dw_user_analytics.sql", BQ_CLIENT)
    
    print("Pipeline execution completed successfully!")
    

