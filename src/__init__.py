import numpy as np
import matplotlib.pyplot as plt


NUMBER_POINTS_PER_PERIOD = 20


def generate_trapezoidal_signal(number_periods: int,
                                frequency: float,
                                high_value: float,
                                low_value: float,
                                rise_time_percent: float,
                                high_time_percent: float,
                                fall_time_percent: float,
                                low_time_percent: float,
                                show_graph: bool):

    if (rise_time_percent + high_time_percent + fall_time_percent + low_time_percent) != 1:
        raise Exception("Sum of percentages cannot be different than 1")

    amplitude = high_value - low_value

    points_rise = int(rise_time_percent * NUMBER_POINTS_PER_PERIOD)
    points_high = int(high_time_percent * NUMBER_POINTS_PER_PERIOD)
    points_fall = int(fall_time_percent * NUMBER_POINTS_PER_PERIOD)
    points_low = int(low_time_percent * NUMBER_POINTS_PER_PERIOD)

    signal_period = np.zeros(NUMBER_POINTS_PER_PERIOD)
    t1 = points_rise
    for i in range(t1):
        signal_period[i] = low_value + (i * amplitude / points_rise)

    t2 = t1 + points_high
    for i in range(t1, t2):
        signal_period[i] = high_value

    t3 = t2 + points_fall
    for i in range(t2, t3):
        signal_period[i] = high_value - ((i - t2) * amplitude / points_fall)

    t4 = t3 + points_low
    for i in range(t3, t4):
        signal_period[i] = low_value

    signal = np.tile(signal_period, number_periods)

    if show_graph:
        total_time = NUMBER_POINTS_PER_PERIOD * number_periods * (1 / frequency)

        # Plotting the generated signal
        time = np.linspace(0, total_time, len(signal))
        plt.plot(time, signal)
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude (V)')
        plt.title('Trapezoidal Signal')
        plt.grid(True)
        plt.show()

    return signal


if __name__ == "__main__":
    # Example usage:
    number_periods = 1
    frequency = 1000  # Hz
    high_value = 5    # Volts
    low_value = -5    # Volts
    rise_time_percent = 0.1  # percentage of period
    high_time_percent = 0.4  # percentage of period
    fall_time_percent = 0.1  # percentage of period
    low_time_percent = 0.4  # percentage of period

    generated_signal = generate_trapezoidal_signal(
        number_periods=number_periods,
        frequency=frequency,
        high_value=high_value,
        low_value=low_value,
        rise_time_percent=rise_time_percent,
        high_time_percent=high_time_percent,
        fall_time_percent=fall_time_percent,
        low_time_percent=low_time_percent,
        show_graph=True
    )
    print(generated_signal)
