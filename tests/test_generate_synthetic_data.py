import pandas as pd
import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../src/traders_copilot_mzza_25'))
from data import generate_synthetic_data

def test_dataframe_structure():
    """Test the structure of the generated DataFrame."""
    df = generate_synthetic_data("2022-01-01", "2022-12-31", num_records=252, seed=524)
    assert isinstance(df, pd.DataFrame), "The output is not a pandas DataFrame!"
    expected_columns = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]
    assert list(df.columns) == expected_columns, "The DataFrame does not have the expected columns!"

def test_dataframe_nulls():
    """Test that the DataFrame has no missing values."""
    df = generate_synthetic_data("2022-01-01", "2022-12-31", num_records=252, seed=524)
    assert not df.isnull().values.any(), "The DataFrame contains null values!"

def test_data_types():
    """Test if the columns in the DataFrame are numeric."""
    df = generate_synthetic_data("2022-01-01", "2022-12-31", num_records=252, seed=524)
    numeric_columns = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]
    for col in numeric_columns:
        assert pd.api.types.is_numeric_dtype(df[col]), f"Column '{col}' is not numeric!"

def test_date_format():
    """Test that the function raises an error for invalid date formats."""
    with pytest.raises(ValueError, match="Invalid date format"):
        generate_synthetic_data("2022/01/01", "2022-12-31")
    with pytest.raises(ValueError, match="Invalid date format"):
        generate_synthetic_data("01-01-2022", "12-31-2022")

def test_single_record():
    """Ensure function works when generating a single record."""
    df = generate_synthetic_data("2023-01-01", "2023-01-01", num_records=1, seed=42)
    assert df.shape[0] == 1, "The function should generate exactly one record."

def test_zero_records():
    """Ensure function raises an error for num_records=0."""
    with pytest.raises(ValueError, match="num_records must be greater than 0"):
        generate_synthetic_data("2023-01-01", "2023-12-31", num_records=0)

def test_invalid_date_range():
    """Ensure function raises an error when start_date > end_date."""
    with pytest.raises(ValueError, match="start_date must be before end_date"):
        generate_synthetic_data("2025-12-31", "2023-01-01", num_records=252)

def test_random_seed_consistency():
    """Ensure using the same seed produces the same results."""
    df1 = generate_synthetic_data("2023-01-01", "2023-12-31", num_records=252, seed=100)
    df2 = generate_synthetic_data("2023-01-01", "2023-12-31", num_records=252, seed=100)
    pd.testing.assert_frame_equal(df1, df2, check_dtype=True)
