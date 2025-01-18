import pandas as pd

def generate_signals(data):
    """
    Generate buy/sell signals based on SMA and RSI.

    Parameters:
    - data (pd.DataFrame): DataFrame that includes 'SMA_50', 'SMA_200', and 'RSI' columns.

    Returns:
    - pd.DataFrame: DataFrame with a new 'Signal' column (Buy, Sell, Hold).
    """

    if not isinstance(data, pd.DataFrame):
        raise TypeError('Data object is not a type of dataframe.')

    required_columns = ['SMA_50', 'SMA_200', 'RSI']
    if not all(column in data.columns for column in required_columns):
        raise ValueError(f"DataFrame must contain the following columns: {', '.join(required_columns)}")

    data['Signal'] = 'HOLD'
    data.loc[(data['SMA_50'] > data['SMA_200']) & (data['RSI'] < 30), 'Signal'] = 'BUY'
    data.loc[(data['SMA_50'] < data['SMA_200']) & (data['RSI'] > 70), 'Signal'] = 'SELL'

    return data
