import pandas as pd
from utils.data_utils import clean_data, convert_to_datetime


class BrentOilData:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)

    def preprocess(self):
        # Convert Date column to datetime format
        self.data = convert_to_datetime(self.data, date_column="Date")

        # Handle missing values
        self.data = clean_data(self.data)

        # Sort by date
        self.data.sort_values("Date", inplace=True)
        self.data.reset_index(drop=True, inplace=True)

    def get_data(self):
        return self.data
