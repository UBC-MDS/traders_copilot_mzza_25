from datetime import datetime
import matplotlib.pyplot as plt

def validate_lengths(price, time):
    """Ensure the lengths of the price and time lists match."""
    if len(price) != len(time):
        raise ValueError("The lengths of 'price' and 'time' must match.")

def validate_non_empty(price, time):
    """Ensure both price and time are non-empty."""
    if not price or not time:
        raise ValueError("Both 'price' and 'time' must be non-empty lists.")

def validate_dates(time):
    """Validate that each time string is in the 'YYYY-MM-DD' format."""
    for date in time:
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Ensure all date strings are in 'YYYY-MM-DD' format.")

def generate_plot(price, time):
    """Generate a Matplotlib figure for the price vs. time data."""
    fig, ax = plt.subplots()
    ax.plot(time, price, marker='o')
    ax.set_title("Price vs. Time")
    ax.set_xlabel("Time")
    ax.set_ylabel("Price")
    plt.xticks(rotation=45)
    return fig

def plot_signals(price, time):
    """
    Plot a time series depicting the price at specific timestamps.
    
    Parameters
    ----------
    price : list of float
        A list of price values.
    time : list of str
        A list of timestamps corresponding to the price values, formatted as 'YYYY-MM-DD'.
    
    Returns
    -------
    matplotlib.figure.Figure
        The Matplotlib figure object containing the time series plot.
    
    Raises
    ------
    ValueError
        If the lengths of 'price' and 'time' do not match.
        If 'price' or 'time' is an empty list.
        If any date in 'time' is not in the 'YYYY-MM-DD' format.
    
    Examples
    --------
    >>> price = [100, 102, 104]
    >>> time = ["2023-01-01", "2023-01-02", "2023-01-03"]
    >>> fig = plot_signals(price, time)
    >>> fig.show()
    """
    validate_lengths(price, time)
    validate_non_empty(price, time)
    validate_dates(time)
    return generate_plot(price, time)
    