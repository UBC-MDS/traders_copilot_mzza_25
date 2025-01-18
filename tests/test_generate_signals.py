import pytest
import sys
import os
import pandas as pd
sys.path.append(os.path.join(os.path.dirname(__file__), '../src/traders_copilot_mzza_25'))
from generate_signals import generate_signals


@pytest.fixture
def mock_data():
    data = {
        'SMA_50': [40, 40, 40],
        'SMA_200': [40, 40, 40],
        'RSI': [50, 50, 50]
    }
    return pd.DataFrame(data)


@pytest.fixture
def mock_data_missing_columns():
    data = {
        'SMA_200': [40, 40, 40],
        'RSI': [50, 50, 50]
    }
    return pd.DataFrame(data)


def test_generate_signals_invalid_param_object():
    """Test invalid data types."""
    with pytest.raises(TypeError, match='Data object is not a type of dataframe.'):
        generate_signals('10')
    with pytest.raises(TypeError, match='Data object is not a type of dataframe.'):
        generate_signals(10)
    with pytest.raises(TypeError, match='Data object is not a type of dataframe.'):
        generate_signals([1, 2, 3])
    with pytest.raises(TypeError, match='Data object is not a type of dataframe.'):
        generate_signals({'1', '2'})


def test_missing_column(mock_data_missing_columns):
    """Test missing columns."""
    with pytest.raises(ValueError, match='DataFrame must contain the following columns'):
        generate_signals(mock_data_missing_columns)


def test_generate_signals_buy_signal(mock_data):
    """Test buy signals."""
    mock_data.loc[0, 'SMA_50'] = 50
    mock_data.loc[0, 'SMA_200'] = 30
    mock_data.loc[0, 'RSI'] = 20
    result = generate_signals(mock_data)
    assert result.loc[0, 'Signal'] == 'BUY'


def test_generate_signals_sell_signal(mock_data):
    """Test buy signals."""
    mock_data.loc[0, 'SMA_50'] = 30
    mock_data.loc[0, 'SMA_200'] = 50
    mock_data.loc[0, 'RSI'] = 80
    result = generate_signals(mock_data)
    assert result.loc[0, 'Signal'] == 'SELL'


def test_generate_signals_mixed_signals(mock_data):
    """Test mixed signals."""
    mock_data.loc[0, 'SMA_50'] = 50
    mock_data.loc[0, 'SMA_200'] = 30
    mock_data.loc[0, 'RSI'] = 20
    mock_data.loc[1, 'SMA_50'] = 30
    mock_data.loc[1, 'SMA_200'] = 50
    mock_data.loc[1, 'RSI'] = 80
    mock_data.loc[2, 'SMA_50'] = 40
    mock_data.loc[2, 'SMA_200'] = 40
    mock_data.loc[2, 'RSI'] = 50
    result = generate_signals(mock_data)
    assert result.loc[0, 'Signal'] == 'BUY'
    assert result.loc[1, 'Signal'] == 'SELL'
    assert result.loc[2, 'Signal'] == 'HOLD'


def test_generate_signals_no_signals(mock_data):
    """Test no signals change."""
    result = generate_signals(mock_data)
    assert all(result['Signal'] == 'HOLD')