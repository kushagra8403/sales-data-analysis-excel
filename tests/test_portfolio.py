from pathlib import Path
import subprocess
import sys
import pandas as pd

ROOT = Path(__file__).parents[1]
PROJECTS = {
    "02-customer-churn-analysis": "customers.csv",
    "03-ecommerce-funnel-analysis": "sessions.csv",
    "04-marketing-campaign-analysis": "campaigns.csv",
    "05-operations-workforce-analysis": "workforce.csv",
    "06-executive-bi-dashboard": "executive_kpis.csv",
}


def test_generators_create_non_empty_data():
    for project, filename in PROJECTS.items():
        folder = ROOT / project
        subprocess.run([sys.executable, "src/generate_data.py"], cwd=folder, check=True)
        path = folder / "data" / filename
        assert path.exists(), f"Missing generated dataset: {path}"
        df = pd.read_csv(path)
        assert not df.empty, f"Generated dataset is empty: {path}"
        assert df.columns.is_unique, f"Duplicate columns: {path}"


def test_generated_data_has_no_duplicate_primary_keys():
    keys = {
        "02-customer-churn-analysis": ("customers.csv", "customer_id"),
        "03-ecommerce-funnel-analysis": ("sessions.csv", "session_id"),
        "04-marketing-campaign-analysis": ("campaigns.csv", "campaign_id"),
        "05-operations-workforce-analysis": ("workforce.csv", "employee_id"),
        "06-executive-bi-dashboard": ("executive_kpis.csv", "month"),
    }
    for project, (filename, key) in keys.items():
        df = pd.read_csv(ROOT / project / "data" / filename)
        assert df[key].notna().all(), f"Null primary key values in {project}"
        assert not df[key].duplicated().any(), f"Duplicate primary keys in {project}"
