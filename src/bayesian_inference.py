import pymc3 as pm
import numpy as np


class BayesianModel:
    def __init__(self, data):
        self.data = data

    def fit_bayesian_model(self):
        with pm.Model() as model:
            # Priors
            mu = pm.Normal("mu", mu=0, sigma=1)
            sigma = pm.HalfNormal("sigma", sigma=1)

            # Likelihood
            y = pm.Normal("y", mu=mu, sigma=sigma, observed=self.data["Price"])

            # Sampling
            trace = pm.sample(1000, return_inferencedata=True)
        return trace
