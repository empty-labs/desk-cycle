# 3rd party packages
import matplotlib.pyplot as plt
import numpy as np


def set_marker_colors(exercise):
    """Set marker colors by resistance level

    Args:
        exercise: DeskCycleData class

    Returns:
        colors (list): list of marker colors
    """

    colors = []

    for i in range(len(exercise.resistance)):
        if exercise.resistance[i] == 1:
            colors.append('lightgreen')
        elif exercise.resistance[i] == 2:
            colors.append('yellowgreen')
        elif exercise.resistance[i] == 3:
            colors.append('gold')
        elif exercise.resistance[i] == 4:
            colors.append('darkorange')
        elif exercise.resistance[i] == 5:
            colors.append('crimson')
        else:
            colors.append('black')

    return colors


def plot_mph_rate(exercise):
    """Set marker colors by resistance level

    Args:
        exercise: DeskCycle exercise set

    Returns
        colors (list): list of marker colors
    """
    # Plot distance (mi) / time (min) rate by resistance
    colors = set_marker_colors(exercise=exercise)

    plt.scatter(x=exercise.date, y=exercise.mph_rate, c=colors)
    plt.xlabel("Date")
    plt.ylabel("Velocity (mph)")
    plt.title("MPH Rate")
    plt.show()


def plot_metric_stats_by_timeframe(all_times: list, metric_list: list, metric: str, timeframe: str):
    """Plot time series values for metrics

    Args:
        all_times (list): time values for plot
        metric_list (list): time series values for plot
        metric (str): metric value label
        timeframe (str): timeframe string (yearly, monthly, daily, weekly)
    """

    plt.scatter(x=all_times, y=metric_list)
    plt.xlabel(timeframe)
    plt.ylabel(metric)
    plt.title(f"{metric} by {timeframe}")
    plt.show()


def plot_mph_rate_3d(exercise):
    """Sauce = https://matplotlib.org/stable/gallery/mplot3d/3d_bars.html

    Args:
        exercise: DeskCycleData class
    """

    all_resistance_levels = list(set(exercise.resistance))

    rate = []
    colors = []

    for r in all_resistance_levels:
        for i in range(len(exercise.date)):

            # Rates
            if exercise.resistance[i] == r:
                rate.append(exercise.mph_rate[i])
            else:
                rate.append(0)

            # Colors
            # TODO Consolidate with above
            if exercise.resistance[i] == 1:
                colors.append('lightgreen')
            elif exercise.resistance[i] == 2:
                colors.append('yellowgreen')
            elif exercise.resistance[i] == 3:
                colors.append('gold')
            elif exercise.resistance[i] == 4:
                colors.append('darkorange')
            elif exercise.resistance[i] == 5:
                colors.append('crimson')
            else:
                colors.append('black')

    _x = range(len(exercise.date))
    _y = all_resistance_levels

    _xx, _yy = np.meshgrid(_x, _y)
    x, y = _xx.ravel(), _yy.ravel()

    top = rate
    bottom = np.zeros_like(top)
    width = depth = 1

    # set up the figure and Axes
    fig = plt.figure(figsize=(8, 3))
    ax1 = fig.add_subplot(121, projection='3d')

    ax1.bar3d(x, y, bottom, width, depth, top, shade=True, color=colors)
    ax1.view_init(ax1.elev, ax1.azim + 90)  # Rotate so resistance + events are inverted
    ax1.set_title('MPH Rate by Resistance')
    ax1.set_xlabel('Event No.')
    ax1.set_ylabel('Resistance Level')
    ax1.set_zlabel('Velocity (mph)')

    plt.show()
