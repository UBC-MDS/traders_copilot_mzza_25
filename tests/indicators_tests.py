import pytest
import pandas as pd
import numpy as np
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../src/traders_copilot_mzza_25'))
from indicators import calculate_sma, calculate_rsi
# Test class for calculate_sma and calculate_rsi
class TestIndicators:

    def setup_method(self):
        """Set up test data."""
        self.data = pd.DataFrame({
            'Close': [100, 102, 104, 106, 108, 110, 112, 114, 116, 118]
        })
    
    def test_sma_valid(self):
        """Test SMA calculation with valid data."""
        result = calculate_sma(self.data, window=3)
        assert 'SMA_3' in result.columns
        assert result['SMA_3'].iloc[2] == 102.0  # The average of first 3 values
    
    def test_rsi_valid(self):
        """Test RSI calculation with valid data."""
        result = calculate_rsi(self.data, window=3)
        assert 'RSI' in result.columns
        assert isinstance(result['RSI'].iloc[2], float)
    
    def test_sma_invalid_data_type(self):
        """Test SMA with invalid data type."""
        with pytest.raises(TypeError):
            calculate_sma("invalid data", window=3)
    
    def test_rsi_invalid_data_type(self):
        """Test RSI with invalid data type."""
        with pytest.raises(TypeError):
            calculate_rsi("invalid data", window=3)
    
    def test_sma_missing_close_column(self):
        """Test SMA when 'Close' column is missing."""
        data_missing_close = pd.DataFrame({'Open': [100, 102, 104, 106]})
        with pytest.raises(ValueError):
            calculate_sma(data_missing_close, window=3)
    
    def test_rsi_missing_close_column(self):
        """Test RSI when 'Close' column is missing."""
        data_missing_close = pd.DataFrame({'Open': [100, 102, 104, 106]})
        with pytest.raises(ValueError):
            calculate_rsi(data_missing_close, window=3)

    def test_sma_fillna(self):
        """Test SMA with NaN handling (backfilling)."""
        result = calculate_sma(self.data, window=5, fillna=True)
        assert not result['SMA_5'].isna().any(), "NaNs were not handled properly in SMA with fillna."
    
    def test_rsi_fillna(self):
        """Test RSI with NaN handling (backfilling)."""
        result = calculate_rsi(self.data, window=5, fillna=True)
        assert not result['RSI'].isna().any(), "NaNs were not handled properly in RSI with fillna."
    
    def test_sma_no_fill(self):
        """Test SMA without NaN handling (should leave NaNs)."""
        result = calculate_sma(self.data, window=5, fillna=False)
        assert result['SMA_5'].iloc[:4].isna().all(), "NaNs should exist in the first few rows."
        assert not result['SMA_5'].iloc[4:].isna().any(), "NaNs should not exist after the initial rows."
    
    def test_rsi_no_fill(self):
        """Test RSI without NaN handling (should leave NaNs)."""
        result = calculate_rsi(self.data, window=5, fillna=False)
        assert result['RSI'].iloc[:4].isna().all(), "NaNs should exist in the first few rows."
        assert not result['RSI'].iloc[4:].isna().any(), "NaNs should not exist after the initial rows."
    
    def test_sma_invalid_window(self):
        """Test SMA with an invalid window size."""
        with pytest.raises(ValueError):
            calculate_sma(self.data, window=-1)
        
        with pytest.raises(ValueError):
            calculate_sma(self.data, window="invalid")
    
    def test_rsi_invalid_window(self):
        """Test RSI with an invalid window size."""
        with pytest.raises(ValueError):
            calculate_rsi(self.data, window=-1)
        
        with pytest.raises(ValueError):
            calculate_rsi(self.data, window="invalid")

    def test_empty_dataframe_sma(self):
        """Test SMA with an empty DataFrame."""
        empty_data = pd.DataFrame({'Close': []})
        result = calculate_sma(empty_data, window=3)
        assert 'SMA_3' not in result.columns, "SMA should not be calculated for empty data."
    
    def test_empty_dataframe_rsi(self):
        """Test RSI with an empty DataFrame."""
        empty_data = pd.DataFrame({'Close': []})
        result = calculate_rsi(empty_data, window=3)
        assert 'RSI' not in result.columns, "RSI should not be calculated for empty data."

    def test_sma_window_larger_than_data(self):
        """Test SMA when window size is larger than the number of data points."""
        data_small = pd.DataFrame({'Close': [100, 102]})
        result = calculate_sma(data_small, window=5, fillna=True)
        assert result['SMA_5'].isna().all(), "SMA should return NaNs when the window is larger than the data."

    def test_rsi_window_larger_than_data(self):
        """Test RSI when window size is larger than the number of data points."""
        data_small = pd.DataFrame({'Close': [100, 102]})
        result = calculate_rsi(data_small, window=5, fillna=True)
        assert result['RSI'].isna().all(), "RSI should return NaNs when the window is larger than the data."
    

if __name__ == "__main__":
    pytest.main()