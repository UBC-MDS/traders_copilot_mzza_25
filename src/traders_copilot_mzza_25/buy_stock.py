def buy_stock(account, stock_symbol, quantity, price):
    """Execute a stock purchase and update the user's account.

    This function processes the purchase of a specific quantity of a stock at a given price.
    It updates the user's account balance and increases the number of shares held for
    the specified stock.

    Parameters
    ----------
    account : dict
        A dictionary representing the user's account. Expected keys include:
        - 'balance': float, the current cash balance in the account.
        - 'stocks': dict, mapping stock symbols to the number of shares held.
    stock_symbol : str
        The symbol of the stock being purchased (e.g., 'AAPL', 'GOOG').
    quantity : int
        The number of shares to buy. Must be a positive integer.
    price : float
        The price per share at which the stock is purchased.

    Returns
    -------
    dict
        The updated account dictionary reflecting the new balance and stock holdings.

    Raises
    ------
    ValueError
        If the account balance is insufficient to complete the purchase.

    Examples
    --------
    """