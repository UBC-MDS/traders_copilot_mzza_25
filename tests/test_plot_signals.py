import pytest
from datetime import datetime
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../src/traders_copilot_mzza_25'))
from plot_signals import plot_signals, validate_lengths, validate_non_empty, validate_dates, generate_plot

def test_validate_lengths():
    # Valid input
    validate_lengths([100, 102, 104], ["2023-01-01", "2023-01-02", "2023-01-03"])
    # Mismatched lengths
    with pytest.raises(ValueError, match="The lengths of 'price' and 'time' must match."):
        validate_lengths([100, 102], ["2023-01-01", "2023-01-02", "2023-01-03"])

def test_validate_non_empty():
    # Non-empty lists
    validate_non_empty([100, 102, 104], ["2023-01-01", "2023-01-02", "2023-01-03"])
    # Empty lists
    with pytest.raises(ValueError, match="Both 'price' and 'time' must be non-empty lists."):
        validate_non_empty([], [])

def test_validate_dates():
    # Valid dates
    validate_dates(["2023-01-01", "2023-01-02", "2023-01-03"])
    # Invalid date
    with pytest.raises(ValueError, match="Ensure all date strings are in 'YYYY-MM-DD' format."):
        validate_dates(["2023-01-01", "2023-01-32", "2023-01-03"])

def test_generate_plot():
    # Generate a plot and check if the figure is returned
    fig = generate_plot([100, 102, 104], ["2023-01-01", "2023-01-02", "2023-01-03"])
    assert fig is not None, "The function should return a Matplotlib figure."

def test_plot_signals():
    # Valid input
    price = [100, 102, 104]
    time = ["2023-01-01", "2023-01-02", "2023-01-03"]
    fig = plot_signals(price, time)
    assert fig is not None, "The function should return a Matplotlib figure."

    # Test mismatched lengths
    with pytest.raises(ValueError, match="The lengths of 'price' and 'time' must match."):
        plot_signals([100, 102], ["2023-01-01", "2023-01-02", "2023-01-03"])

    # Test empty lists
    with pytest.raises(ValueError, match="Both 'price' and 'time' must be non-empty lists."):
        plot_signals([], [])

    # Test invalid date format
    with pytest.raises(ValueError, match="Ensure all date strings are in 'YYYY-MM-DD' format."):
        plot_signals([100, 102, 104], ["2023-01-01", "2023-01-32", "2023-01-03"])