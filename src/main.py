from src.data_preprocessing import BrentOilData
from src.time_series_models import TimeSeriesModel
from src.bayesian_inference import BayesianModel
from utils.visualization_utils import plot_time_series
from utils.data_utils import clean_data, convert_to_datetime


def main():
    """
    Main function to execute the entire pipeline:
    1. Load and preprocess the data.
    2. Visualize the time series.
    3. Fit ARIMA and GARCH models.
    4. Perform Bayesian inference.
    """
    # Step 1: Load and preprocess data
    data_loader = BrentOilData("data/raw_data.csv")
    data_loader.preprocess()
    data = data_loader.get_data()

    # Step 2: Visualize the time series
    plot_time_series(data, title="Brent Oil Prices Over Time")

    # Step 3: Fit ARIMA and GARCH models
    ts_model = TimeSeriesModel(data)
    arima_results = ts_model.fit_arima(order=(5, 1, 0))
    garch_results = ts_model.fit_garch(p=1, q=1)

    print("ARIMA Model Summary:")
    print(arima_results.summary())
    print("\nGARCH Model Summary:")
    print(garch_results.summary())

    # Step 4: Perform Bayesian inference
    bayesian_model = BayesianModel(data)
    trace = bayesian_model.fit_bayesian_model()

    # Save results (optional)
    # Further analysis and reporting can be added here


if __name__ == "__main__":
    main()
