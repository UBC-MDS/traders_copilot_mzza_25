def generate_signals(prices):
    """Identify buy and sell signals based on price trends.

    A buy signal is generated when the price is lower than its previous value,
    and a sell signal is generated when the price is higher than its previous value.

    Parameters
    ----------
    prices : list of float
        A list of price values.

    Returns
    -------
    dict
        A dictionary with two keys: 'buy_signals' and 'sell_signals', containing
        indices of buy and sell signals respectively.
    
    Examples
    --------
    
    """
    