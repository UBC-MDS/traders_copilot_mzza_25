import pytest
import pandas as pd
from datetime import datetime
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../src/traders_copilot_mzza_25'))
from plot_signals import plot_signals, validate_lengths, validate_non_empty, validate_dates, generate_plot, validate_columns

@pytest.fixture
def sample_data():
    """Provide sample DataFrame for testing."""
    return pd.DataFrame({
        "Date": ["2023-01-01", "2023-01-02", "2023-01-03"],
        "Close": [100, 102, 104]
    })

def test_validate_columns(sample_data):
    """Test that the DataFrame contains required columns."""
    validate_columns(sample_data, "Close", "Date")
    with pytest.raises(ValueError, match="The DataFrame must contain 'Price' and 'Date' columns."):
        validate_columns(sample_data, "Price", "Date")

def test_validate_lengths(sample_data):
    """Test that price and time columns have matching lengths."""
    # Valid lengths should pass
    validate_lengths(sample_data, "Close", "Date")

    # Create mismatched lengths by dropping rows from one column
    mismatched_data = sample_data.copy()
    mismatched_data.loc[1, "Date"] = None  # Introduce a missing value in 'Date'

    # Expect a ValueError due to mismatched lengths
    with pytest.raises(ValueError, match="The lengths of 'price' and 'time' columns must match."):
        validate_lengths(mismatched_data, "Close", "Date")

def test_validate_non_empty(sample_data):
    """Test that price and time columns are non-empty."""
    validate_non_empty(sample_data, "Close", "Date")
    with pytest.raises(ValueError, match="Both 'price' and 'time' columns must be non-empty."):
        validate_non_empty(pd.DataFrame({"Date": [], "Close": []}), "Close", "Date")

def test_validate_dates(sample_data):
    """Test that all dates are in 'YYYY-MM-DD' format."""
    validate_dates(sample_data, "Date")
    with pytest.raises(ValueError, match="Ensure all dates in 'Date' are in 'YYYY-MM-DD' format."):
        invalid_data = sample_data.copy()
        invalid_data.loc[1, "Date"] = "2023-01-32"
        validate_dates(invalid_data, "Date")

def test_generate_plot(sample_data):
    """Test that generate_plot returns a Matplotlib figure."""
    fig = generate_plot(sample_data["Close"], sample_data["Date"])
    assert fig is not None, "The function should return a Matplotlib figure."

def test_plot_signals(sample_data):
    """Test the end-to-end plot_signals function."""
    fig = plot_signals(sample_data)
    assert fig is not None, "The function should return a Matplotlib figure."

    with pytest.raises(ValueError, match="The DataFrame must contain 'Price' and 'Date' columns."):
        plot_signals(sample_data, price_col="Price")
