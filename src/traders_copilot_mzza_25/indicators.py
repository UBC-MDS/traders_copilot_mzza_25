import pandas as pd
import numpy as np

#SMA
def calculate_sma(data, window=50, fillna=False):
    """
    Calculate the Simple Moving Average (SMA) for the given data.

    Args:
        data (pd.DataFrame): DataFrame containing stock price data with a 'Close' column.
        window (int): The number of periods to calculate the SMA (default is 50).
        fillna (bool): Whether to fill NaN values (default is False).

    Returns:
        pd.DataFrame: DataFrame with an additional column for the SMA.
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("The input data must be a pandas DataFrame.")
    
    if 'Close' not in data.columns:
        raise ValueError("The input DataFrame must contain a 'Close' column.")
    
    # Calculate the rolling mean (SMA)
    data[f'SMA_{window}'] = data['Close'].rolling(window=window).mean()
    
    # Handle NaNs 
    if fillna:
        data[f'SMA_{window}'] = data[f'SMA_{window}'].bfill()  
    
    return data

#RSI 
def calculate_rsi(data, window=14, fillna=False):
    """
    Calculate the Relative Strength Index (RSI) measuring the speed and change of price movements.

    Args:
        data (pd.DataFrame): DataFrame containing stock price data with a 'Close' column.
        window (int): Number of periods for RSI calculation (default is 14).
        fillna (bool): Whether to fill NaN values (default is False).

    Returns:
        pd.DataFrame: DataFrame with an additional column for RSI.
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("The input data must be a pandas DataFrame.")
    
    if 'Close' not in data.columns:
        raise ValueError("The input DataFrame must contain a 'Close' column.")
    
    delta = data['Close'].diff()
    
    # Separate gains and losses
    gain = (delta.where(delta > 0, 0)).fillna(0)
    loss = (-delta.where(delta < 0, 0)).fillna(0)
    
    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()
    rs = avg_gain / avg_loss
    
    # Calculate the RSI
    data['RSI'] = 100 - (100 / (1 + rs))
    
    # Handle NaNs 
    if fillna:
        data['RSI'] = data['RSI'].bfill()  
    
    return data
