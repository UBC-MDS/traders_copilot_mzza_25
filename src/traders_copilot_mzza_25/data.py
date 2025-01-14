import yfinance as yf

def fetch_data(ticker, start_date, end_date):
    """
    Fetch historical stock data using yfinance.

    Args:
        ticker (str): Stock ticker symbol.
        start_date (str): Start date for data retrieval in YYYY-MM-DD format.
        end_date (str): End date for data retrieval in YYYY-MM-DD format.

    Returns:
        pandas.DataFrame: DataFrame containing stock data.

    """
    data = yf.download(ticker, start=start_date, end=end_date)
    if data.empty:
        raise ValueError(f"No data found.")
    return data

def clean_data(data):
    """
    Clean and process stock data.

    Args:
        data (pandas.DataFrame): Raw stock data.

    Returns:
        pandas.DataFrame: Cleaned stock data with additional metrics.
    """
    # Drop rows with missing values
    data = data.dropna()

    # Calculate daily returns
    data['Daily_Return'] = data['Close'].pct_change()

    return data
