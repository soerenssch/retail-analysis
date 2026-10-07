import pandas as pd

from retail_analysis.prepare_data import normalize_ids


def test_normalize_ids_removes_outer_whitespace():
    values = pd.Series([" C001 ", "C002 "])

    assert normalize_ids(values).tolist() == ["C001", "C002"]


def test_normalize_ids_normalizes_case():
    ids = pd.Series(["c001"])

    result = normalize_ids(ids)

    assert result.tolist() == ["C001"]


def test_normalize_ids_works_in_a_small_dataframe():
    orders = pd.DataFrame({"customer_id": [" c001 ", "C002 ", " c003"]})

    orders["customer_id"] = normalize_ids(orders["customer_id"])

    assert orders["customer_id"].tolist() == ["C001", "C002", "C003"]
