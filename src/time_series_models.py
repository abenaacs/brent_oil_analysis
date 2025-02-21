import pandas as pd
from utils.model_utils import fit_arima_model, fit_garch_model


class TimeSeriesModel:
    """
    A class to handle fitting ARIMA and GARCH models to time series data.

    Attributes:
        data (pd.DataFrame): The dataset containing time series data.
    """

    def __init__(self, data):
        """
        Initializes the TimeSeriesModel class with the given dataset.

        Parameters:
            data (pd.DataFrame): Dataset containing time series data.
        """
        self.data = data

    def fit_arima(self, order=(1, 1, 1)):
        """
        Fits an ARIMA model to the time series data.

        Parameters:
            order (tuple): The (p, d, q) order of the ARIMA model.

        Returns:
            ARIMAResults: Fitted ARIMA model.
        """
        return fit_arima_model(self.data, order=order)

    def fit_garch(self, p=1, q=1):
        """
        Fits a GARCH model to the time series data.

        Parameters:
            p (int): The GARCH p parameter.
            q (int): The GARCH q parameter.

        Returns:
            ARCHModelResult: Fitted GARCH model.
        """
        return fit_garch_model(self.data, p=p, q=q)
