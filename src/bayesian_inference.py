import pymc3 as pm
import numpy as np


class BayesianModel:
    """
    A class to perform Bayesian inference on time series data using PyMC3.

    Attributes:
        data (pd.DataFrame): The dataset containing time series data.

    Methods:
        fit_bayesian_model(): Fits a Bayesian model to the data and returns the trace.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the BayesianModel class with the given dataset.

        Parameters:
            data (pd.DataFrame): Dataset containing time series data.
        """
        self.data = data

    def fit_bayesian_model(self):
        """
        Fits a Bayesian model to the time series data using PyMC3.

        The model assumes a normal likelihood with priors on the mean (`mu`) and standard deviation (`sigma`).

        Returns:
            trace: The posterior samples from the Bayesian inference.
        """
        with pm.Model() as model:
            # Priors
            mu = pm.Normal("mu", mu=0, sigma=1)  # Prior for the mean
            sigma = pm.HalfNormal("sigma", sigma=1)  # Prior for the standard deviation

            # Likelihood (observed data)
            y = pm.Normal("y", mu=mu, sigma=sigma, observed=self.data["Price"])

            # Sampling from the posterior
            trace = pm.sample(1000, return_inferencedata=True)

        return trace
