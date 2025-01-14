import pandas as pd
import numpy as np

def generate_synthetic_data(start_date, end_date, num_records=252, seed=524):
    """
    Generate synthetic stock data.

    Args:
        start_date (str): Start date in YYYY-MM-DD format.
        end_date (str): End date in YYYY-MM-DD format.
        num_records (int): Number of records to generate 
                          (default is 252 trading days in a year in major stock markets).
        seed (int): Random seed for reproducibility.

    Returns:
        pandas.DataFrame
    """
    np.random.seed(seed)
    
    # Generate dates
    dates = pd.date_range(start=start_date, end=end_date, periods=num_records)
    
    # Simulate a random walk for stock prices
    prices = np.cumsum(np.random.normal(0, 1, num_records)) + 100  #1starting at $100 per share 
    
    
    high = prices + np.random.uniform(0.5, 2.0, num_records)
    low = prices - np.random.uniform(0.5, 2.0, num_records)
    open_price = prices + np.random.uniform(-1.0, 1.0, num_records)
    adj_close = prices * (1 + np.random.uniform(-0.01, 0.01, num_records))
    volume = np.random.randint(1_000_000, 5_000_000, num_records)
    
    # Create a DataFrame
    data = pd.DataFrame({
        "Date": dates,
        "Open": open_price,
        "High": high,
        "Low": low,
        "Close": prices,
        "Adj Close": adj_close,
        "Volume": volume
    })
    
    
    data.set_index("Date", inplace=True)
    
    return stock_data