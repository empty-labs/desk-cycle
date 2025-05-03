# 3rd party packages
import numpy as np

# Constants
MIN_PER_HR = 60


def extract_days_between_events(date):
    """Grab days between events

    Args:
        date (list)

    Returns
        days_between_events (list)
    """

    days_between_events = []
    for i in range(1, len(date)):
        days_between_events.append((date[i] - date[i - 1]).days)

    return days_between_events


def distance_per_calorie_by_resistance(distance: list, calories: list, resistance: list, match_resistance: float):
    """Get distance / calorie metric by each resistance level

    Args:
        distance (list)
        calories (list)
        resistance (list)
        match_resistance (float)

    Returns:
        distance_per_calorie (float)
    """
    distance_per_calorie_list = []

    for i in range(len(distance)):
        if distance[i] != "" and calories[i] != "" and resistance[i] == match_resistance:
            distance_per_calorie_list.append(distance[i] / calories[i])

    distance_per_calorie = np.mean(distance_per_calorie_list)

    return distance_per_calorie


def interpolate_distance(distance: list, calories: list, resistance: list, time: list, metrics_dict: dict):
    """Fill in missing data using metrics dictionary

    Args:
        distance (list)
        calories (list)
        resistance (list)
        time (list)
        metrics_dict (dict)

    Returns:
        distance_list (float)
    """

    for i in range(len(distance)):
        if distance[i] == "":
            if calories[i] == "":
                calories[i] = metrics_dict[resistance[i]]["calories_per_time"] * time[i]

            distance[i] = metrics_dict[resistance[i]]["distance_per_calorie"] * calories[i]

    return distance, calories


def create_metrics_dict(distance: list, calories: list, resistance: list, time: list):
    """Generate metrics dictionary

    Args:
        distance (list)
        calories (list)
        resistance (list)
        time (list)

    Returns:
        metrics_dict (dict)
    """
    metrics_dict = {}
    all_resistances = set(resistance)

    for res in all_resistances:
        distance_per_calorie = distance_per_calorie_by_resistance(
            distance=distance, calories=calories, resistance=resistance, match_resistance=res)

        avg_dist_per_time = metric_average_per_time_by_resistance(
            metric=distance, time=time, resistance=resistance, match_resistance=res)

        avg_cals_per_time = metric_average_per_time_by_resistance(
            metric=calories, time=time, resistance=resistance, match_resistance=res)

        metrics_dict[res] = {"distance_per_calorie": 0, "distance_per_time": 0, "calories_per_time": 0}
        metrics_dict[res]["distance_per_calorie"] = distance_per_calorie
        metrics_dict[res]["distance_per_time"] = avg_dist_per_time
        metrics_dict[res]["calories_per_time"] = avg_cals_per_time

    return metrics_dict


def metric_average(metric: list):
    """Take average of metrics where not empty

    Args:
        metric (list)

    Returns:
        average (float)
    """

    metric_list = [x for x in metric if x != ""]
    return np.mean(metric_list)


def metric_average_by_resistance(metric: list, resistance: list, match_resistance: float):
    """Take average of metrics where not empty

    Args:
        metric (list)
        resistance (list)
        match_resistance (list)

    Returns:
        average (float)
    """

    metric_list = []
    for i in range(len(metric)):
        if resistance[i] == match_resistance and metric[i] != "":
            metric_list.append(metric[i])

    return np.mean(metric_list)


def metric_average_per_time_by_resistance(metric: list, time: list, resistance: list, match_resistance: float):
    """Take average of metrics where not empty

    Args:
        metric (list)
        time (list)
        resistance (list)
        match_resistance (list)

    Returns:
        average (float)
    """

    metric_sum = 0
    time_sum = 0
    for i in range(len(metric)):
        if resistance[i] == match_resistance and metric[i] != "":
            metric_sum += metric[i]
            time_sum += time[i]

    return metric_sum / time_sum


def calculate_mph_rate(exercise):
    """Grab velocity (mph)

    Args:
        exercise: DeskCycleData class

    Returns
        rate (list)
    """

    rate = []
    for i in range(len(exercise.distance)):
        rate.append(exercise.distance[i] / exercise.time[i])
        # Convert
        rate[i] *= MIN_PER_HR

    return rate
