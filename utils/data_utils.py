import pandas as pd


def clean_data(df):
    """
    Cleans the dataset by handling missing values.

    Parameters:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    # Forward-fill missing values
    df["Price"].fillna(method="ffill", inplace=True)
    return df


def convert_to_datetime(df, date_column):
    """
    Converts a column to datetime format.

    Parameters:
        df (pd.DataFrame): Input DataFrame.
        date_column (str): Name of the date column.

    Returns:
        pd.DataFrame: DataFrame with converted date column.
    """
    df[date_column] = pd.to_datetime(df[date_column], format="%d-%b-%y")
    return df
