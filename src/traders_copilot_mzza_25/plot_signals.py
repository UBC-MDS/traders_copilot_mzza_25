import matplotlib.pyplot as plt
from datetime import datetime

def plot_signals(price, time):
    """Plot a timeseries plot depicting the timestamp for a price at a point in time.

    Parameters
    ----------
    price : list of float
        A list of price values.
    time : list of datetime or list of str
        A list of timestamps corresponding to the price values.

    Returns
    -------
    matplotlib.figure.Figure
        The Matplotlib figure object containing the time series plot.

    Examples
    --------
    """
    if not price or not time:
        raise ValueError("Both 'price' and 'time' must be non-empty lists.")

    if len(price) != len(time):
        raise ValueError("The lengths of 'price' and 'time' must match.")

    # Convert time to datetime if needed
    try:
        time = [datetime.strptime(t, '%Y-%m-%d') if isinstance(t, str) else t for t in time]
    except ValueError as e:
        raise ValueError("Ensure all date strings are in 'YYYY-MM-DD' format.") from e

    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(time, price, label="Price", color="blue", marker="o")
    ax.set_title("Price Over Time")
    ax.set_xlabel("Time")
    ax.set_ylabel("Price")
    ax.grid(True)
    ax.legend()

    return fig

# Integration with synthetic data generation
def main():
    from data import generate_synthetic_data

    # Generate synthetic data
    data = generate_synthetic_data("2023-01-01", "2023-12-31")

    # Extract Date and Close prices
    time = data.index.to_list()
    price = data["Close"].to_list()

    # Plot the data
    fig = plot_signals(price, time)
    fig.savefig("time_series_plot.png")

if __name__ == "__main__":
    main()