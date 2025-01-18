import pytest
import pandas as pd
import numpy as np
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../src/traders_copilot_mzza_25'))
from indicators import calculate_sma, calculate_rsi


@pytest.fixture
def setup_data():
    """Set up test data."""
    return pd.DataFrame({
        'Close': [100, 102, 104, 106, 108, 110, 112, 114, 116, 118]
    })

def test_sma_valid(setup_data):
    """Test SMA calculation with valid data."""
    result = calculate_sma(setup_data, window=3)
    assert 'SMA_3' in result.columns
    assert result['SMA_3'].iloc[2] == 102.0  # The average of first 3 values

def test_rsi_valid(setup_data):
    """Test RSI calculation with valid data."""
    result = calculate_rsi(setup_data, window=3)
    assert 'RSI' in result.columns
    assert isinstance(result['RSI'].iloc[2], float)

def test_sma_invalid_data_type():
    """Test SMA with invalid data type."""
    with pytest.raises(TypeError):
        calculate_sma("invalid data", window=3)

def test_rsi_invalid_data_type():
    """Test RSI with invalid data type."""
    with pytest.raises(TypeError):
        calculate_rsi("invalid data", window=3)

def test_sma_missing_close_column():
    """Test SMA when 'Close' column is missing."""
    data_missing_close = pd.DataFrame({'Open': [100, 102, 104, 106]})
    with pytest.raises(ValueError):
        calculate_sma(data_missing_close, window=3)

def test_rsi_missing_close_column():
    """Test RSI when 'Close' column is missing."""
    data_missing_close = pd.DataFrame({'Open': [100, 102, 104, 106]})
    with pytest.raises(ValueError):
        calculate_rsi(data_missing_close, window=3)

def test_sma_fillna(setup_data):
    """Test SMA with NaN handling (backfilling)."""
    result = calculate_sma(setup_data, window=5, fillna=True)
    assert not result['SMA_5'].isna().any(), "NaNs were not handled properly in SMA with fillna."

def test_rsi_fillna(setup_data):
    """Test RSI with NaN handling (backfilling)."""
    result = calculate_rsi(setup_data, window=5, fillna=True)
    assert not result['RSI'].isna().any(), "NaNs were not handled properly in RSI with fillna."

def test_sma_no_fill(setup_data):
    """Test SMA without NaN handling (should leave NaNs)."""
    result = calculate_sma(setup_data, window=5, fillna=False)
    assert result['SMA_5'].iloc[:4].isna().all(), "NaNs should exist in the first few rows."
    assert not result['SMA_5'].iloc[4:].isna().any(), "NaNs should not exist after the initial rows."

def test_rsi_no_fill(setup_data):
    """Test RSI without NaN handling (should leave NaNs)."""
    result = calculate_rsi(setup_data, window=5, fillna=False)
    assert result['RSI'].iloc[:4].isna().all(), "NaNs should exist in the first few rows."
    assert not result['RSI'].iloc[4:].isna().any(), "NaNs should not exist after the initial rows."

def test_sma_invalid_window(setup_data):
    """Test SMA with an invalid window size."""
    with pytest.raises(ValueError):
        calculate_sma(setup_data, window=-1)

    with pytest.raises(ValueError):
        calculate_sma(setup_data, window="invalid")

def test_rsi_invalid_window(setup_data):
    """Test RSI with an invalid window size."""
    with pytest.raises(ValueError):
        calculate_rsi(setup_data, window=-1)

    with pytest.raises(ValueError):
        calculate_rsi(setup_data, window="invalid")

def test_empty_dataframe_sma():
    """Test SMA with an empty DataFrame."""
    empty_data = pd.DataFrame({'Close': []})
    result = calculate_sma(empty_data, window=3)
    assert 'SMA_3' not in result.columns, "SMA should not be calculated for empty data."

def test_empty_dataframe_rsi():
    """Test RSI with an empty DataFrame."""
    empty_data = pd.DataFrame({'Close': []})
    result = calculate_rsi(empty_data, window=3)
    assert 'RSI' not in result.columns, "RSI should not be calculated for empty data."

def test_sma_window_larger_than_data():
    """Test SMA when window size is larger than the number of data points."""
    data_small = pd.DataFrame({'Close': [100, 102]})
    result = calculate_sma(data_small, window=5, fillna=True)
    assert result['SMA_5'].isna().all(), "SMA should return NaNs when the window is larger than the data."

def test_rsi_window_larger_than_data():
    """Test RSI when window size is larger than the number of data points."""
    data_small = pd.DataFrame({'Close': [100, 102]})
    result = calculate_rsi(data_small, window=5, fillna=True)
    assert result['RSI'].isna().all(), "RSI should return NaNs when the window is larger than the data."
