# 3rd party packages
from datetime import datetime

# Constants
MONTH_TO_YEAR = 1 / 12


def extract_datetime(data):
    """Grab date

    Args:
        data: data set

    Returns
        datetime_values (list): list of datetime objects
    """

    datetime_values = []

    for i in range(len(data.index)):
        datetime_values.append(datetime.strptime(data.loc[i, "Date"], '%m/%d/%y'))

    return datetime_values


def extract_year_month(date: list):
    """Grab year month from date

    Args:
        date (list)

    Returns
        year_month (list)
    """

    # Monthly
    return [d.year + d.month * MONTH_TO_YEAR for d in date]


def extract_year(date: list):
    """Grab year from date

    Args:
        date (list)

    Returns
        year (list)
    """

    # Yearly
    return [d.year for d in date]


def extract_weekday(date: list):
    """Grab day of the week from date

    Args:
        date (list)

    Returns
        year (list)
    """

    # Weekday
    weekday_mapping = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}

    return [weekday_mapping[d.weekday()] for d in date]


def extract_week(date: list):
    """Grab day of the week from date

    Args:
        date (list)

    Returns
        year (list)
    """

    start_date = min(date)
    return [int((d - start_date).days / 7) for d in date]
