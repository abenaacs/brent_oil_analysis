import statsmodels.api as sm
from arch import arch_model


def fit_arima_model(data, order=(1, 1, 1)):
    """
    Fits an ARIMA model to the data.

    Parameters:
        data (pd.DataFrame): Input DataFrame with 'Price' column.
        order (tuple): ARIMA order (p, d, q).

    Returns:
        ARIMAResults: Fitted ARIMA model.
    """
    model = sm.tsa.ARIMA(data["Price"], order=order)
    results = model.fit()
    return results


def fit_garch_model(data, p=1, q=1):
    """
    Fits a GARCH model to the data.

    Parameters:
        data (pd.DataFrame): Input DataFrame with 'Price' column.
        p (int): GARCH p parameter.
        q (int): GARCH q parameter.

    Returns:
        ARCHModelResult: Fitted GARCH model.
    """
    returns = data["Price"].pct_change().dropna()
    garch_model = arch_model(returns, vol="GARCH", p=p, q=q)
    results = garch_model.fit(disp="off")
    return results
