# traders_copilot_mzza_25

[![Documentation Status](https://readthedocs.org/projects/traders-copilot-mzza-25/badge/?version=latest)](https://traders-copilot-mzza-25.readthedocs.io/en/latest/?badge=latest)

This package is a streamlined application designed to assist in investment decision-making. It provides trading signals for stock markets by leveraging two key technical indicators: Simple Moving Average (SMA), which smooths price data to identify trends, and Relative Strength Index (RSI), which measures the speed and magnitude of price movements to determine overbought or oversold conditions.

## Contributors

Mingyang Zhang, Zanan Pech, Ziyuan Zhao and Abeba Nigussie Turi

## Installation

1.  Clone the Repository git clone <https://github.com/UBC-MDS/traders_copilot_mzza_25.git> cd traders_copilot_mzza_25

2.  Install the Package: \$ pip install traders_copilot_mzza_25

## Usage

`traders_copilot_mzza_25` can be used to simulate market data, generate trading signals, and visualize results. Here are examples of usage:

### Simulate Market Data

``` python
from traders_copilot_mzza_25 import simulate_market_data

# Simulate stock market data
synthetic_data = simulate_market_data(start_date="2023-01-01", end_date="2023-12-31", num_records=252)
print(synthetic_data.head())
```

### Calculate Indicators

``` python
from traders_copilot_mzza_25 import calculate_sma, calculate_rsi

# Calculate SMA and RSI
synthetic_data = calculate_sma(synthetic_data, window=50)
synthetic_data = calculate_rsi(synthetic_data, window=14)
print(synthetic_data.head())
```

### Generate Trading Signals

``` python
from traders_copilot_mzza_25 import generate_signals

# Generate buy/sell signals
signals = generate_signals(synthetic_data)
print(signals[['SMA_50', 'SMA_200', 'RSI', 'Signal']].head())
```

### Visualize Signals

``` python
from traders_copilot_mzza_25 import plot_signals

# Plot signals
fig = plot_signals(signals, price_col="Close", time_col="Date")
fig.show()
```

## Features

traders_copilot_mzza_25 package is a specialized tool for traders and investors fitting into a Python ecosystem of a similar vein. The package augments the existing trading and financial analysis packages like TA-Lib, Backtrader, and PyAlgoTrade by combining trading signal generation, strategy optimization, and built-in visualization tools into one place for a comprehensive trading workflow.

-   **simulate_market_data:** Simulates stock market data for analysis and testing.
-   **Technical Indicators:** Implements:
    -   Simple Moving Average (SMA): Smooths price data to identify trends.
    -   Relative Strength Index (RSI): Measures the speed and magnitude of price movements to assess overbought/oversold conditions.
-   **generate_signals:** Identifies buy/sell signals based on SMA and RSI thresholds:
    -   **Buy Signal:**
        -   SMA_50 \> SMA_200 (short-term trend is stronger)
        -   RSI \< 30 (stock is oversold)
    -   **Sell Signal:**
        -   SMA_50 \< SMA_200 (long-term trend is stronger)
        -   RSI \> 70 (stock is overbought)
-   **plot_signals:** Visualizes stock data with buy/sell signals marked on the chart.

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`traders_copilot_mzza_25` was created by Mingyang Zhang, Zanan Pech, Ziyuan Zhao and Abeba Nigussie Turi. It is licensed under the terms of the MIT license.

## Credits

`traders_copilot_mzza_25` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
