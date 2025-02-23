from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error


def fit_arima_model(data, order=(1, 1, 1)):
    """
    Fits an ARIMA model to the time series data.

    Parameters:
        data (pd.Series): Time series data.
        order (tuple): (p, d, q) order of the ARIMA model.

    Returns:
        ARIMAResults: Fitted ARIMA model.
    """
    model = ARIMA(data, order=order)
    results = model.fit()
    return results


def evaluate_model(y_true, y_pred):
    """
    Evaluates model performance using RMSE.

    Parameters:
        y_true (array-like): True values.
        y_pred (array-like): Predicted values.

    Returns:
        float: RMSE value.
    """
    rmse = mean_squared_error(y_true, y_pred, squared=False)
    return rmse
