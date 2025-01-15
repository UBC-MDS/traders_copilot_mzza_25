import pytest
import pandas as pd
import numpy as np
\import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from traders_copilot_mzza_25.indicators import calculate_sma, calculate_rsi
# Test class for calculate_sma and calculate_rsi
class TestIndicators:
    
    def setup_method(self):
        """Set up test data for the test cases."""
        self.data = pd.DataFrame({
            'Close': [100, 102, 104, 106, 108, 110, 112, 114, 116, 118]
        })
    
    def test_sma_with_nan_handling(self):
        """Test SMA with NaN handling (forward fill, backward fill, or leave NaNs)."""
        # Call the function to calculate SMA
        result = calculate_sma(self.data, window=3, fillna=True)
        
        # Check that NaNs are filled by backfilling if fillna=True
        assert not result['SMA_3'].isna().any(), "NaNs were not handled properly in SMA."
    
    def test_sma_with_no_fill(self):
        """Test SMA with no NaN handling (should leave NaNs)."""
        result = calculate_sma(self.data, window=3, fillna=False)
        
        # Check that NaNs remain (first few rows should have NaN)
        assert result['SMA_3'].iloc[:2].isna().all(), "NaNs should exist in the first few rows."

    def test_rsi_with_nan_handling(self):
        """Test RSI with NaN handling (forward fill, backward fill, or leave NaNs)."""
        result = calculate_rsi(self.data, window=3, fillna=True)
        
        # Check that NaNs are filled by backfilling if fillna=True
        assert not result['RSI'].isna().any(), "NaNs were not handled properly in RSI."
    
    def test_rsi_with_no_fill(self):
        """Test RSI with no NaN handling (should leave NaNs)."""
        result = calculate_rsi(self.data, window=3, fillna=False)
        
        # Check that NaNs remain (first few rows should have NaN)
        assert result['RSI'].iloc[:2].isna().all(), "NaNs should exist in the first few rows."

    def test_sma_invalid_window(self):
        """Test SMA with an invalid window size (should raise ValueError)."""
        with pytest.raises(ValueError):
            calculate_sma(self.data, window=-1)
        
        with pytest.raises(ValueError):
            calculate_sma(self.data, window="string")
     
    def test_rsi_invalid_window(self):
        """Test RSI with an invalid window size (should raise ValueError)."""
        with pytest.raises(ValueError):
            calculate_rsi(self.data, window=-1)
        
        with pytest.raises(ValueError):
            calculate_rsi(self.data, window="string")

if __name__ == "__main__":
    pytest.main()