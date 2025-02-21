import pandas as pd
import statsmodels.api as sm
from arch import arch_model


class TimeSeriesModel:
    def __init__(self, data):
        self.data = data

    def fit_arima(self, order=(1, 1, 1)):
        model = sm.tsa.ARIMA(self.data["Price"], order=order)
        results = model.fit()
        return results

    def fit_garch(self, p=1, q=1):
        returns = self.data["Price"].pct_change().dropna()
        garch_model = arch_model(returns, vol="GARCH", p=p, q=q)
        results = garch_model.fit(disp="off")
        return results
