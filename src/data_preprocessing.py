import pandas as pd
from utils.data_utils import clean_data, convert_to_datetime


class BrentOilData:
    """
    A class to handle loading, preprocessing, and cleaning of Brent oil price data.

    Attributes:
        data (pd.DataFrame): The dataset containing Brent oil prices.
    """

    def __init__(self, file_path):
        """
        Initializes the BrentOilData class with the dataset from the given file path.

        Parameters:
            file_path (str): Path to the raw data file.
        """
        self.data = pd.read_csv(file_path)

    def preprocess(self):
        """
        Preprocesses the dataset by converting the 'Date' column to datetime format,
        handling missing values, and sorting the data by date.
        """
        # Convert Date column to datetime format
        self.data = convert_to_datetime(self.data, date_column="Date")

        # Handle missing values
        self.data = clean_data(self.data)

        # Sort by date and reset index
        self.data.sort_values("Date", inplace=True)
        self.data.reset_index(drop=True, inplace=True)

    def get_data(self):
        """
        Returns the preprocessed dataset.

        Returns:
            pd.DataFrame: The cleaned and preprocessed dataset.
        """
        return self.data
