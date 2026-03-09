import pandas as pd
import logging

logging.basicConfig(
    filename="../logs/inventory.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_inventory(path):
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        logging.error(f"Error loading inventory file: {e}")
        raise

def load_sales(path):
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        logging.error(f"Error loading sales file: {e}")
        raise