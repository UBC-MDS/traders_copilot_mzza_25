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
