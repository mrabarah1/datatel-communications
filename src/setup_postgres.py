import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv  


load_dotenv()

user = os.getenv("PG_USER")
password = os.getenv("PG_PASSWORD")
host = os.getenv("PG_HOST")
port = os.getenv("PG_PORT")
db = os.getenv("PG_DATABASE")

conn_string = f"postgresql://{user}:{password}@{host}:{port}/{db}"

# Create the engine
engine = create_engine(conn_string)

def load_csv_to_postgres():
    files = {
        "src_customers":"src/src_customers.csv",
        "src_billing_transactions":"src/src_billing_transactions.csv",
        "src_network_sessions":"src/src_network_sessions.csv"
    }
    []
    for table, file in files.items():
        print(f"Loading {file} to {table}...")
        # Extracts raw data from CSV
        df = pd.read_csv(file)
        
        # Performs a tiny transformation to ensure date fields are in string format for PostgreSQL
        if 'transaction_date' in df.columns:
            df['transaction_date'] = df['transaction_date'].astype(str)
        
        # Loads the extracted data directly into PostgreSQL    
        df.to_sql(table, engine, if_exists='replace', index=False)
        print(f"{table} loaded successfully")
        
        

            