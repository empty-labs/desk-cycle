# 3rd party packages
import pandas as pd

# Local packages
import Tools.exercise_utils as ex
import Tools.date_utils as du
import Tools.csv_utils as csvu

# Constants\
DESK_CYCLE_FILEPATH = r"Data/DeskCycle.csv"


class DeskCycleData:

    def __init__(self):
        data = pd.read_csv(DESK_CYCLE_FILEPATH, header=0)

        # Baseline
        self.data = data
        self.date = []
        self.year_month = []
        self.year = []
        self.days_between_events = []
        self.weekday = []
        self.week = []
        self.time = []
        self.calories = []
        self.distance = []
        self.resistance = []
        # self.notes = []

        # Derived
        self.metrics_dict = {}
        self.mph_rate = []

    def set_data(self):
        # Assume missing resistance values = 3
        self.data.loc[0:5, "Resistance"] = 3

        self.date = du.extract_datetime(data=self.data)
        self.year_month = du.extract_year_month(date=self.date)
        self.year = du.extract_year(date=self.date)
        self.days_between_events = ex.extract_days_between_events(date=self.date)
        self.weekday = du.extract_weekday(date=self.date)
        self.week = du.extract_week(date=self.date)
        self.time = csvu.extract_values_by_header(data=self.data, main_field="Minutes", sub_field="Seconds")
        self.calories = csvu.extract_values_by_header(data=self.data, main_field="Calories")
        self.distance = csvu.extract_values_by_header(data=self.data, main_field="Distance")
        self.resistance = csvu.extract_values_by_header(data=self.data, main_field="Resistance")
        self.clean_up_missing_distance()

        self.mph_rate = ex.calculate_mph_rate(exercise=self)

    def clean_up_missing_distance(self):
        """Interpolate distance values for all available resistances using metrics"""

        self.metrics_dict = ex.create_metrics_dict(
            distance=self.distance, calories=self.calories, resistance=self.resistance, time=self.time)

        self.distance, self.calories = ex.interpolate_distance(
            distance=self.distance, calories=self.calories, resistance=self.resistance, time=self.time,
            metrics_dict=self.metrics_dict)
