# 3rd party packages
import numpy as np

# Distance Constants
EARTH_CIRCUMFERENCE_MI = 24901
EARTH_TO_MOON_MI = 238900
MARATHON_MI = 26.2

# Calories Constants
CALORIES_TO_POUNDS = 1 / 3500
# https://en.wikipedia.org/wiki/TNT_equivalent
JOULES_PER_KILOCALORIE = 4184  # Food calorie = kilocalorie
JOULES_PER_TNT_GRAM = JOULES_PER_KILOCALORIE
JOULES_PER_TNT_TON = (10 ** 6) * JOULES_PER_KILOCALORIE

# https://www.theverge.com/2023/9/15/23874884/iphone-15-pro-bigger-battery-capacity-increase
# https://www.reddit.com/r/theydidthemath/comments/693daq/request_how_many_calories_would_it_take_to_charge/?rdt=58551
JOULES_PER_WATT_HOURS = 3600
IPHONE_15_PRO_BATTERY_CAPACITY_WATT_HOURS = 12.70

# Drinks Constants
OLYMPIC_POOL_VOLUME_GALLONS = 660000
BEER_BARREL_GALLONS = 55
OIL_DRUM_GALLONS = 42
BEER_KEG_GALLONS = 15.5
BEER_OUNCES = 12
GALLONS_TO_OUNCES = 128


def calculate_year_month_stats(exercise):
    """Determine monthly stats for distance, calories

    Args:
        exercise: DeskCycleData class

    Returns
        all_year_months (list)
        year_month_distance_list (list)
        year_month_calories_list (list)
        year_month_days_between_events_list (list)
    """

    all_year_months = list(set(exercise.year_month))

    year_month_distance_list = []
    year_month_calories_list = []
    year_month_days_between_events_list = []

    # TODO Could convert to dictionary to skip for loop
    for ym in all_year_months:

        year_month_distance = 0
        year_month_calories = 0
        year_month_days_between_events = 0
        events = 0

        for i in range(len(exercise.date)):

            if exercise.year_month[i] == ym:
                year_month_distance += exercise.distance[i]
                year_month_calories += exercise.calories[i]
                if i > 0:
                    year_month_days_between_events += exercise.days_between_events[i-1]
                    events += 1

        year_month_distance_list.append(year_month_distance)
        year_month_calories_list.append(year_month_calories)
        if events == 0:
            year_month_days_between_events_list.append(year_month_days_between_events)
        else:
            year_month_days_between_events_list.append(year_month_days_between_events / events)

    print("\nAverage Monthly Distance: {} miles".format(round(np.mean(year_month_distance_list), 2)))
    print("Average Monthly Calories: {} cals".format(round(np.mean(year_month_calories_list), 2)))
    print("Average Monthly Days Between Events: {} days".format(round(np.mean(year_month_days_between_events_list), 2)))

    return all_year_months, year_month_distance_list, year_month_calories_list, year_month_days_between_events_list,


# TODO: Consolidate with above?
def calculate_yearly_stats(exercise):
    """Determine yearly stats for distance, calories

    Args:
        exercise: DeskCycleData class

    Returns
        all_years (list)
        year_distance_list (list)
        year_calories_list (list)
        year_days_between_events_list (list)
    """

    all_years = list(set(exercise.year))

    year_distance_list = []
    year_calories_list = []
    year_days_between_events_list = []

    # TODO Could convert to dictionary to skip for loop
    for y in all_years:

        year_distance = 0
        year_calories = 0
        year_days_between_events = 0
        events = 0

        for i in range(len(exercise.date)):

            if exercise.year[i] == y:
                year_distance += exercise.distance[i]
                year_calories += exercise.calories[i]
                if i > 0:
                    year_days_between_events += exercise.days_between_events[i-1]
                    events += 1

        year_distance_list.append(year_distance)
        year_calories_list.append(year_calories)
        if events == 0:
            year_days_between_events_list.append(year_days_between_events)
        else:
            year_days_between_events_list.append(year_days_between_events / events)

    print("\nAverage Yearly Distance: {} miles".format(round(np.mean(year_distance_list), 2)))
    print("Average Yearly Calories: {} cals".format(round(np.mean(year_calories_list), 2)))
    print("Average Yearly Days Between Events: {} days".format(round(np.mean(year_days_between_events_list), 2)))

    return all_years, year_distance_list, year_calories_list, year_days_between_events_list


# TODO: Consolidate with above?
def calculate_weekly_stats(exercise):
    """Determine weekly stats for distance, calories

    Args:
        exercise: DeskCycleData class

    Returns
        all_weeks (list)
        week_distance_list (list)
        week_calories_list (list)
        week_days_between_events_list (list)
    """

    all_weeks = list(set(exercise.week))

    week_distance_list = []
    week_calories_list = []
    week_days_between_events_list = []

    # TODO Could convert to dictionary to skip for loop
    for w in all_weeks:

        week_distance = 0
        week_calories = 0
        week_days_between_events = 0
        events = 0

        for i in range(len(exercise.date)):

            if exercise.week[i] == w:
                week_distance += exercise.distance[i]
                week_calories += exercise.calories[i]
                if i > 0:
                    week_days_between_events += exercise.days_between_events[i-1]
                    events += 1

        week_distance_list.append(week_distance)
        week_calories_list.append(week_calories)
        if events == 0:
            week_days_between_events_list.append(week_days_between_events)
        else:
            week_days_between_events_list.append(week_days_between_events / events)

    print("\nAverage Weekly Distance: {} miles".format(round(np.mean(week_distance_list), 2)))
    print("Average Weekly Calories: {} cals".format(round(np.mean(week_calories_list), 2)))
    print("Average Weekly Days Between Events: {} days".format(round(np.mean(week_days_between_events_list), 2)))

    return all_weeks, week_distance_list, week_calories_list, week_days_between_events_list


def calculate_total_stats(exercise):
    """Determine overall stats for distance, calories

    Args:
        exercise: DeskCycleData class

    Returns
        total_distance (float)
        total_calories (float)
        total_days_between_events (float)
    """
    total_distance = 0
    total_calories = 0
    total_days_between_events = 0
    events = 0

    for i in range(len(exercise.date)):
        total_distance += exercise.distance[i]
        total_calories += exercise.calories[i]
        if i > 0:
            total_days_between_events += exercise.days_between_events[i-1]
            events += 1

    print("\nTotal Distance: {} miles".format(round(total_distance, 2)))
    print("Total Calories: {} cals".format(round(total_calories, 2)))
    print("\nAverage Distance: {} miles".format(round(total_distance / len(exercise.date), 2)))
    print("Average Calories: {} cals".format(round(total_calories / len(exercise.date), 2)))
    if events > 0:
        print("Average days between events: {}".format(round(total_days_between_events / events, 2)))

    return total_distance, total_calories, total_days_between_events


def calculate_year_month_drink_stats(beers):
    """Determine monthly stats for drinks

    Args:
        beers: DrinkData class

    Returns
        all_year_months (list)
        year_month_drinks_list (list)
    """

    all_year_months = list(set(beers.year_month))

    year_month_drinks_list = []

    # TODO Could convert to dictionary to skip for loop and consolidate with DeskCycle
    for ym in all_year_months:

        year_month_drinks = 0

        for i in range(len(beers.date)):

            if beers.year_month[i] == ym:
                year_month_drinks += beers.drinks[i]

        year_month_drinks_list.append(year_month_drinks)

    print("\nAverage Monthly Drinks: {} drinks".format(round(np.mean(year_month_drinks_list), 2)))

    return all_year_months, year_month_drinks_list


def calculate_weekly_drink_stats(beers):
    """Determine weekly stats for drinks

    Args:
        beers: DrinkData class

    Returns
        all_weeks (list)
        weekly_drinks_list (list)
    """

    all_weeks = list(set(beers.week))

    weekly_drinks_list = []

    # TODO Could convert to dictionary to skip for loop and consolidate with DeskCycle
    for w in all_weeks:

        weekly_drinks = 0

        for i in range(len(beers.date)):

            if beers.week[i] == w:
                weekly_drinks += beers.drinks[i]

        weekly_drinks_list.append(weekly_drinks)

    print("\nAverage Weekly Drinks: {} drinks".format(round(np.mean(weekly_drinks_list), 2)))

    return all_weeks, weekly_drinks_list


# TODO: Consolidate with above?
def calculate_yearly_drink_stats(beers):
    """Determine yearly stats for drinks

    Args:
        beers: DrinkData class

    Returns
        all_years (list)
        year_drinks_list (list)
        normalized_year_drinks_list (list)
    """

    all_years = list(set(beers.year))

    year_drinks_list = []
    normalized_year_drinks_list = []

    # TODO Could convert to dictionary to skip for loop
    for y in all_years:

        year_drinks = 0
        days = 0

        for i in range(len(beers.date)):

            if beers.year[i] == y:
                year_drinks += beers.drinks[i]
                days += 1

        year_drinks_list.append(year_drinks)
        normalized_year_drinks_list.append(year_drinks * (365.25 / days))

    print("\nAverage Yearly Drinks: {} drinks".format(round(np.mean(year_drinks_list), 2)))
    print("Average Yearly Drinks (normalized): {} drinks".format(round(np.mean(normalized_year_drinks_list), 2)))

    return all_years, year_drinks_list, normalized_year_drinks_list


# TODO: Consolidate with above?
def calculate_weekday_drink_stats(beers, year: float = None):
    """Determine weekday stats for drinks, by year if specified

    Args:
        beers: DrinkData class
        year (float): during specific year

    Returns
        all_weekdays (list)
        weekday_drinks_list (list)
        weekday_average_drinks_list (list)
    """

    # TODO Save somewhere, date_utils?
    weekday_mapping = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    all_weekdays = weekday_mapping.values()

    weekday_drinks_list = []
    weekday_average_drinks_list = []

    # TODO Could convert to dictionary to skip for loop
    for w in all_weekdays:

        weekday_drinks = 0
        weekday_count = 0

        for i in range(len(beers.date)):

            if beers.weekday[i] == w:
                if year is not None:
                    if beers.year[i] == year:
                        weekday_drinks += beers.drinks[i]
                        weekday_count += 1
                else:
                    weekday_drinks += beers.drinks[i]
                    weekday_count += 1

        weekday_drinks_list.append(weekday_drinks)
        if weekday_count > 0:
            average_drinks = weekday_drinks / weekday_count
            weekday_average_drinks_list.append(average_drinks)

        if year is not None:
            print("\nTotal {} Drinks ({}): {} drinks".format(w, year, round(weekday_drinks, 2)))
            if weekday_count > 0:
                print("Average {} Drinks ({}): {} drinks".format(w, year, round(np.mean(average_drinks), 2)))
        else:
            print("\nTotal {} Drinks: {} drinks".format(w, round(weekday_drinks, 2)))
            if weekday_count > 0:
                print("Average {} Drinks: {} drinks".format(w, round(np.mean(average_drinks), 2)))

    return all_weekdays, weekday_drinks_list, weekday_average_drinks_list


# TODO: Consolidate with above?
def calculate_weekday_exercise_stats(exercise, year: float = None):
    """Determine weekday stats for drinks, by year if specified

    Args:
        exercise: DeskCycleData class
        year (float): during specific year

    Returns
        all_weekdays (list)
        weekday_drinks_list (list)
        weekday_average_drinks_list (list)
    """

    # TODO Save somewhere, date_utils?
    weekday_mapping = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    all_weekdays = weekday_mapping.values()

    weekday_events_list = []
    weekday_average_distance_list = []

    # TODO Could convert to dictionary to skip for loop
    for w in all_weekdays:

        weekday_events = 0
        weekday_count = 0

        for i in range(len(exercise.date)):

            if exercise.weekday[i] == w:
                if year is not None:
                    if exercise.year[i] == year:
                        weekday_events += exercise.distance[i]
                        weekday_count += 1
                else:
                    weekday_events += exercise.distance[i]
                    weekday_count += 1

        weekday_events_list.append(weekday_events)
        if weekday_count > 0:
            average_distance = weekday_events / weekday_count
            weekday_average_distance_list.append(average_distance)

        if year is not None:
            print("\nTotal {} Events ({}): {} events".format(w, year, weekday_count))
            if weekday_count > 0:
                print("Average {} Distance ({}): {} miles".format(w, year, round(np.mean(average_distance), 2)))
        else:
            print("\nTotal {} Events: {} events".format(w, weekday_count, 2))
            if weekday_count > 0:
                print("Average {} Distance: {} miles".format(w, round(np.mean(average_distance), 2)))

    return all_weekdays, weekday_events_list, weekday_average_distance_list


def calculate_total_drink_stats(beers):
    """Determine overall stats for drinks

    Args:
        beers: DrinkData class

    Returns
        total_drinks (float)
    """
    total_drinks = 0

    for i in range(len(beers.date)):
        total_drinks += beers.drinks[i]

    print("\nTotal Drinks: {} drinks".format(round(total_drinks, 2)))
    print("Average Drinks: {} drinks".format(round(total_drinks / len(beers.date), 2)))

    return total_drinks


def print_interesting_distance_stats(total_distance: float):
    """
    Args:
        total_distance (float)
    """
    print("\nTotal Earth Distances: {} Earths".format(round(total_distance / EARTH_CIRCUMFERENCE_MI, 2)))
    print("Total Earth-Moon Distances: {} Earth-Moons".format(round(total_distance / EARTH_TO_MOON_MI, 2)))
    print("Total Marathons: {} Marathons".format(round(total_distance / MARATHON_MI, 2)))


def print_interesting_calories_stats(total_calories: float):
    """
    Args:
        total_calories (float)
    """
    print("\nTotal Pounds: {} lbs".format(round(total_calories * CALORIES_TO_POUNDS, 2)))
    print("Total grams of TNT: {} g".format(round(total_calories * JOULES_PER_KILOCALORIE / JOULES_PER_TNT_GRAM, 2)))
    print("Total tons of TNT: {} tons".format(round(total_calories * JOULES_PER_KILOCALORIE / JOULES_PER_TNT_TON, 5)))
    calories_per_iphone_battery = IPHONE_15_PRO_BATTERY_CAPACITY_WATT_HOURS * JOULES_PER_WATT_HOURS / JOULES_PER_KILOCALORIE
    print("Total iPhone 15 Pro Batteries: {} batteries".format(
        round(total_calories / calories_per_iphone_battery, 2)))


def print_interesting_drinks_stats(total_drinks: float):
    """
    Args:
        total_drinks (float)
    """
    olympic_pools = total_drinks * BEER_OUNCES / (OLYMPIC_POOL_VOLUME_GALLONS * GALLONS_TO_OUNCES)
    print("\nTotal Olympic swimming pools: {} pools".format(round(olympic_pools, 5)))
    beer_barrels = total_drinks * BEER_OUNCES / (BEER_BARREL_GALLONS * GALLONS_TO_OUNCES)
    print("Total Beer Barrels (55 gal): {} barrels".format(round(beer_barrels, 2)))
    oil_drums = total_drinks * BEER_OUNCES / (OIL_DRUM_GALLONS * GALLONS_TO_OUNCES)
    print("Total Oil Barrels (42 gal): {} barrels".format(round(oil_drums, 2)))
    beer_kegs = total_drinks * BEER_OUNCES / (BEER_KEG_GALLONS * GALLONS_TO_OUNCES)
    print("Total Beer Kegs (15.5 gal): {} kegs".format(round(beer_kegs, 2)))

