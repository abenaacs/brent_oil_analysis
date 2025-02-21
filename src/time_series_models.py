import pandas as pd
from utils.model_utils import fit_arima_model, fit_garch_model


class TimeSeriesModel:
    def __init__(self, data):
        self.data = data

    def fit_arima(self, order=(1, 1, 1)):
        return fit_arima_model(self.data, order=order)

    def fit_garch(self, p=1, q=1):
        return fit_garch_model(self.data, p=p, q=q)
