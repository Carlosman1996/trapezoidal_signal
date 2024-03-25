import pytest
from src import main
import numpy as np

def test_happy_path():
    test_signal = np.array([-5, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, -5, -5, -5, -5, -5, -5, -5, -5, -1])

    # Run
    number_periods = 1
    frequency = 1000  # Hz
    high_value = 5    # Volts
    low_value = -5    # Volts
    rise_time_percent = 0.1  # percentage of period
    high_time_percent = 0.4  # percentage of period
    fall_time_percent = 0.1  # percentage of period
    low_time_percent = 0.4  # percentage of period

    generated_signal = main.generate_trapezoidal_signal(
        number_periods=number_periods,
        frequency=frequency,
        high_value=high_value,
        low_value=low_value,
        rise_time_percent=rise_time_percent,
        high_time_percent=high_time_percent,
        fall_time_percent=fall_time_percent,
        low_time_percent=low_time_percent,
        show_graph=False
    )

    np.testing.assert_array_equal(test_signal, generated_signal)
