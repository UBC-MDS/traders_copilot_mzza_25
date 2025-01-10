def sell(account, stock_symbol, quantity, price):
    """Execute a stock sale and update the user's account.

    This function processes the sale of a specific quantity of a stock at a given price.
    It updates the user's account balance and decreases the number of shares held for
    the specified stock.

    Parameters
    ----------
    account : dict
        A dictionary representing the user's account. Expected keys include:
        - 'balance': float, the current cash balance in the account.
        - 'stocks': dict, mapping stock symbols to the number of shares held.
    stock_symbol : str
        The symbol of the stock being sold (e.g., 'AAPL', 'GOOG').
    quantity : int
        The number of shares to sell. Must not exceed the number of shares currently held.
    price : float
        The price per share at which the stock is sold.

    Returns
    -------
    dict
        The updated account dictionary reflecting the new balance and stock holdings.

    Raises
    ------
    ValueError
        If the quantity to sell exceeds the number of shares held for the stock.

    Examples
    --------
    >>> account = {'balance': 1000.0, 'stocks': {'AAPL': 10}}
    >>> sell(account, 'AAPL', 5, 150.0)
    {'balance': 1750.0, 'stocks': {'AAPL': 5}}

    >>> sell(account, 'AAPL', 10, 150.0)
    ValueError: Not enough shares to sell.
    """
