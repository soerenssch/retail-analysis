"""Small reusable helpers for the retail notebook."""

from pathlib import Path

import pandas as pd


def normalize_ids(series: pd.Series) -> pd.Series:
    """Normalize identifier whitespace and casing."""
    return series.str.strip().str.upper()


def load_data(project_root: Path) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Load the three original retail inputs from the project."""
    raw = project_root / "data" / "raw"
    customers = pd.read_csv(raw / "customers.csv")
    orders = pd.read_csv(raw / "orders.csv")
    order_items = pd.read_csv(raw / "order_items.csv")
    return customers, orders, order_items
