# traders_copilot_mzza_25
[![Documentation Status](https://readthedocs.org/projects/traders-copilot-mzza-25/badge/?version=latest)](https://traders-copilot-mzza-25.readthedocs.io/en/latest/?badge=latest)

This package is a streamlined application designed to assist in investment decision-making. It provides trading signals for stock markets by leveraging two key technical indicators: Simple Moving Average (SMA), which smooths price data to identify trends, and Relative Strength Index (RSI), which measures the speed and magnitude of price movements to determine overbought or oversold conditions.


## Contributors

Mingyang Zhang, Zanan Pech, Ziyuan Zhao and Abeba Nigussie Turi

## Installation

1. Clone the Repository
git clone https://github.com/UBC-MDS/traders_copilot_mzza_25.git
cd traders_copilot_mzza_25

2. Install the Package:
$ pip install traders_copilot_mzza_25


## Usage

traders_copilot_mzza_25 provides functionalities for generating trading signals and visualizing trading data. Here are the key functions in this package:

- simulate_market_data: a function that simulate stock market data.
  
Technical Indicators:
Simple Moving Averages (SMA)
Relative Strength Index (RSI)

- generate_signals: a function that identify buy/sell signals based on SMA and RSI thresholds:
  > Buy Signal:
SMA_50 > SMA_200 (short-term trend is stronger)
RSI < 30 (stock is oversold)

> Sell Signal:
SMA_50 < SMA_200 (long-term trend is stronger)
RSI > 70 (stock is overbought)

- plot_signals: function that visualizes the timestamp of the stock with the buy/sell signals.

## Features

traders_copilot_mzza_25 package is a specialized tool for traders and investors fitting into a Python ecosystem of a similar vein. The package augments the existing trading and financial analysis packages like TA-Lib, Backtrader, and PyAlgoTrade by combining trading signal generation, strategy optimization, and built-in visualization tools into one place for a comprehensive trading workflow.


## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`traders_copilot_mzza_25` was created by Mingyang Zhang, Zanan Pech, Ziyuan Zhao and Abeba Nigussie Turi. It is licensed under the terms of the MIT license.

## Credits

`traders_copilot_mzza_25` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
