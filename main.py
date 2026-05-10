from src.setup_postgres import load_csv_to_postgres
from src.validate import run_quality_checks
from src.pipeline import run_pipeline

if __name__ == "__main__":
    load_csv_to_postgres()
    run_quality_checks()
    run_pipeline()