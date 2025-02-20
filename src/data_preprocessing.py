import pandas as pd


class BrentOilData:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)

    def preprocess(self):
        # Convert Date column to datetime format
        self.data["Date"] = pd.to_datetime(self.data["Date"], format="%d-%b-%y")

        # Sort by date
        self.data.sort_values("Date", inplace=True)

        # Handle missing values (forward fill)
        self.data["Price"].fillna(method="ffill", inplace=True)

        # Reset index
        self.data.reset_index(drop=True, inplace=True)

    def get_data(self):
        return self.data
