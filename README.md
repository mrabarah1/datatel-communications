# datatel_pipeline

A lightweight data pipeline that ingests CSV source data into PostgreSQL, performs basic quality validation, and loads the source data into BigQuery for staging, transformation, and warehouse processing.

## Project Overview

This repository demonstrates a multi-stage ETL workflow using:

- PostgreSQL for source data ingestion
- Google BigQuery for analytical processing
- SQL files for staging, transformation, and warehouse layers
- Python orchestration for data loading and pipeline execution

## Setup

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

- mac/linux: `source venv/bin/activate`
- windows: `.\venv\scripts\activate`

- Generate Source Data: Run python `src/generate_data.py` to populate the src/ folder with the necessary CSV files. or open a src folder > and a file called `generate_data.py` then paste this link: '`ttps://drive.google.com/file/d/13m70i4jkBtsfn5xN7g-35FkU4AIJx3qc/view?usp=sharing` to generate raw CSV data

## Repository Structure

- `main.py`: Orchestrates the pipeline end-to-end.
- `requirements.txt`: Python dependency list.
- `src/setup_postgres.py`: Loads source CSV files into PostgreSQL.
- `src/validate.py`: Runs basic data quality checks against PostgreSQL.
- `src/pipeline.py`: Extracts raw data from PostgreSQL, loads it into BigQuery, then executes staging, transformation, and warehouse SQL models.
- `sql/staging/`: SQL models for staging raw source tables.
- `sql/transformations/`: SQL models for producing higher-level aggregates.
- `sql/warehouse/`: Final warehouse model.
- `sql/analysis/`: Example analysis queries.
- `src/`: Contains source CSV data files.

## How It Works

1. `main.py` runs `load_csv_to_postgres()` to load local CSVs into PostgreSQL tables.
2. `main.py` runs `run_quality_checks()` to validate source data quality.
3. `main.py` runs `run_pipeline()` to:
   - extract raw tables from PostgreSQL,
   - load them into BigQuery,
   - execute staging SQL,
   - execute transformation SQL,
   - execute the final warehouse SQL.

## Requirements

- Python 3.8+ (recommended)
- PostgreSQL accessible from the environment
- Google Cloud BigQuery access with credentials configured

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the repository root with the following values:

```env
PG_USER=your_postgres_user
PG_PASSWORD=your_postgres_password
PG_HOST=your_postgres_host
PG_PORT=5432
PG_DATABASE=your_postgres_database
GCP_PROJECT_ID=your_gcp_project_id
BQ_DATASET_ID=your_bigquery_dataset
```

## Running the Pipeline

From the repository root, run:

```bash
python3 main.py
```

This will:

- ingest `src/src_customers.csv`, `src/src_billing_transactions.csv`, and `src/src_network_sessions.csv` into PostgreSQL
- run quality checks against the loaded billing table
- load the source tables into BigQuery
- execute SQL models in `sql/staging/`, `sql/transformations/`, and `sql/warehouse/`

## SQL Layers

- `sql/staging/`: cleans and prepares raw source tables for transformation.
- `sql/transformations/`: builds aggregated datasets such as revenue, usage, ARPU, and session distribution.
- `sql/warehouse/`: builds the final analytics-ready warehouse table `dw_user_analytics`.
- `sql/analysis/`: contains example analysis queries like churn risk, revenue mismatch, and top customers.

## Notes

- The pipeline is currently configured to execute `sql/transformations/session_buckets.sql` during transformation. Add this file if it is missing or update `src/pipeline.py` accordingly.
- Source CSV files are stored under `src/` and loaded directly into PostgreSQL.

## Extending the Pipeline

To extend this project, consider:

- adding more data quality checks in `src/validate.py`
- adding additional SQL models to the staging/transformation layers
- parameterizing table names and query paths for increased flexibility
- adding automated tests for ingestion and SQL execution


## Acknowledgments
- This project was developed as a technical milestone for the AltSchool Africa Data Engineering Program.

- Business Context & Requirements: Provided by AltSchool Africa.

- Implementation & Pipeline Architecture: Developed by Emeka Lawrence Abarah.
