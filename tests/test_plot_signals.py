"""
Unit tests for the plot_signals module.

This test suite verifies the correctness of the helper functions and the main 
plot_signals function from the `plot_signals` module. It includes tests for:
- Length validation of input lists.
- Non-empty validation for inputs.
- Date format validation.
- Plot generation functionality.
- Integration of all validations in the plot_signals function.
"""

import pytest
from datetime import datetime
import sys
import os

# Add the source path to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), '../src/traders_copilot_mzza_25'))
from plot_signals import plot_signals, validate_lengths, validate_non_empty, validate_dates, generate_plot

def test_validate_lengths():
    """
    Test the validate_lengths function to ensure input lists have matching lengths.

    Validates that:
    - Lists of the same length pass without errors.
    - Lists of different lengths raise a ValueError.
    """
    validate_lengths([100, 102, 104], ["2023-01-01", "2023-01-02", "2023-01-03"])
    with pytest.raises(ValueError, match="The lengths of 'price' and 'time' must match."):
        validate_lengths([100, 102], ["2023-01-01", "2023-01-02", "2023-01-03"])

def test_validate_non_empty():
    """
    Test the validate_non_empty function to ensure input lists are not empty.

    Validates that:
    - Non-empty lists pass without errors.
    - Empty lists raise a ValueError.
    """
    validate_non_empty([100, 102, 104], ["2023-01-01", "2023-01-02", "2023-01-03"])
    with pytest.raises(ValueError, match="Both 'price' and 'time' must be non-empty lists."):
        validate_non_empty([], [])

def test_validate_dates():
    """
    Test the validate_dates function to ensure all dates are in 'YYYY-MM-DD' format.

    Validates that:
    - Properly formatted date strings pass without errors.
    - Improperly formatted date strings raise a ValueError.
    """
    validate_dates(["2023-01-01", "2023-01-02", "2023-01-03"])
    with pytest.raises(ValueError, match="Ensure all date strings are in 'YYYY-MM-DD' format."):
        validate_dates(["2023-01-01", "2023-01-32", "2023-01-03"])

def test_generate_plot():
    """
    Test the generate_plot function to ensure it returns a Matplotlib figure.

    Validates that:
    - A valid price and time list generates a non-null figure object.
    """
    fig = generate_plot([100, 102, 104], ["2023-01-01", "2023-01-02", "2023-01-03"])
    assert fig is not None, "The function should return a Matplotlib figure."

def test_plot_signals():
    """
    Test the plot_signals function for end-to-end functionality.

    Validates that:
    - Valid inputs produce a Matplotlib figure.
    - Mismatched list lengths raise a ValueError.
    - Empty lists raise a ValueError.
    - Invalid date formats raise a ValueError.
    """
    price = [100, 102, 104]
    time = ["2023-01-01", "2023-01-02", "2023-01-03"]
    fig = plot_signals(price, time)
    assert fig is not None, "The function should return a Matplotlib figure."

    with pytest.raises(ValueError, match="The lengths of 'price' and 'time' must match."):
        plot_signals([100, 102], ["2023-01-01", "2023-01-02", "2023-01-03"])

    with pytest.raises(ValueError, match="Both 'price' and 'time' must be non-empty lists."):
        plot_signals([], [])

    with pytest.raises(ValueError, match="Ensure all date strings are in 'YYYY-MM-DD' format."):
        plot_signals([100, 102, 104], ["2023-01-01", "2023-01-32", "2023-01-03"])
        