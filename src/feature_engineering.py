import pandas as pd


def create_lagged_features(df, column, lags):
    """
    Creates lagged features for a given column.

    Parameters:
        df (pd.DataFrame): Input dataset.
        column (str): Column name to create lags for.
        lags (list): List of lag values.

    Returns:
        pd.DataFrame: Dataset with lagged features.
    """
    for lag in lags:
        df[f"{column}_lag_{lag}"] = df[column].shift(lag)
    return df


def compute_rolling_statistics(df, column, window):
    """
    Computes rolling statistics (mean, std) for a given column.

    Parameters:
        df (pd.DataFrame): Input dataset.
        column (str): Column name to compute rolling stats for.
        window (int): Rolling window size.

    Returns:
        pd.DataFrame: Dataset with rolling statistics.
    """
    df[f"{column}_rolling_mean"] = df[column].rolling(window=window).mean()
    df[f"{column}_rolling_std"] = df[column].rolling(window=window).std()
    return df
