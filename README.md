# **Brent Oil Price Analysis - Task 1**

## **Overview**

This repository contains the implementation for **Task 1** of the Brent Oil Price Analysis project. The goal of this task is to define the data analysis workflow and understand the models and data that will be used in subsequent tasks. This includes:

- Planning the steps for analyzing Brent oil prices.
- Understanding how the data is generated, sampled, and compiled.
- Familiarizing with statistical models (e.g., ARIMA, GARCH) and Bayesian inference techniques.
- Identifying assumptions, limitations, and expected outputs of the analysis.

---

## **Table of Contents**

1. [Dataset](#dataset)
2. [Installation](#installation)
3. [Directory Structure](#directory-structure)
4. [Data Analysis Workflow](#data-analysis-workflow)
5. [Understanding the Models and Data](#understanding-the-models-and-data)
6. [Assumptions and Limitations](#assumptions-and-limitations)
7. [Expected Outputs](#expected-outputs)

---

## **Dataset**

The dataset contains historical Brent oil prices from **May 20, 1987, to September 30, 2022**. Each record includes:

- **Date**: The date of the recorded price (formatted as `day-month-year`).
- **Price**: The price of Brent oil in USD per barrel.

### **Data Source**

- The dataset is stored in the `data/` directory as `raw_data.csv`.

---

## **Installation**

To set up the project locally, follow these steps:

### **Prerequisites**

- Python 3.8 or higher
- Git

### **Steps**

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/username/brent_oil_analysis.git
   cd brent_oil_analysis
   ```

2. **Install Dependencies**:
   Install the required Python packages using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

3. **Explore the Code**:
   - The source code is located in the `src/` directory.
   - Jupyter notebooks for exploratory analysis are in the `notebooks/` directory.

---

## **Directory Structure**

The project is organized into the following directories and files:

```
brent_oil_analysis/
│
├── data/                     # Raw and processed datasets
│   ├── raw_data.csv          # Raw Brent oil prices dataset
│   └── processed_data.csv    # Processed dataset after cleaning
│
├── src/                      # Source code for analysis
│   ├── data_preprocessing.py # Data cleaning and preprocessing
│   ├── time_series_models.py # Time series models (ARIMA, GARCH)
│   ├── bayesian_inference.py # Bayesian modeling using PyMC3
│   ├── utils.py              # Utility functions (visualization, helpers)
│   └── main.py               # Main script to execute the workflow
│
├── notebooks/                # Jupyter notebooks for exploratory analysis
│   ├── exploratory_analysis.ipynb  # Initial data exploration
│   └── model_evaluation.ipynb      # Model evaluation and insights
│
├── README.md                 # Project overview and instructions
└── requirements.txt          # Python dependencies for the project
```

---

## **Data Analysis Workflow**

The workflow for analyzing Brent oil prices is structured as follows:

### **1. Data Loading and Exploration**

- Load the dataset (`data/raw_data.csv`) into a Pandas DataFrame.
- Perform exploratory data analysis (EDA) to understand trends, seasonality, and anomalies.
- Visualize the time series using Matplotlib or Seaborn.

### **2. Data Preprocessing**

- Handle missing values and outliers.
- Convert the `Date` column to a datetime format.
- Resample the data if necessary (e.g., weekly or monthly averages).

### **3. Statistical Modeling**

- Implement time series models such as ARIMA and GARCH using `statsmodels`.
- Evaluate model performance using metrics like AIC/BIC and residual analysis.

### **4. Bayesian Inference**

- Use PyMC3 to perform Bayesian modeling.
- Define prior distributions for parameters and estimate posterior distributions using MCMC.

### **5. Event Analysis**

- Identify key events (e.g., OPEC meetings, geopolitical conflicts) and their dates.
- Analyze price changes around these events using statistical tests (e.g., t-tests, ANOVA).

---

## **Understanding the Models and Data**

### **Time Series Models**

- **ARIMA**: Captures trends and seasonality in the data.
  - Formula: $ y*t = c + \phi_1 y*{t-1} + \dots + \phi*p y*{t-p} + \epsilon*t - \theta_1 \epsilon*{t-1} - \dots - \theta*q \epsilon*{t-q} $
- **GARCH**: Models volatility clustering in financial time series.
  - Formula: $ \sigma*t^2 = \omega + \alpha \epsilon*{t-1}^2 + \beta \sigma\_{t-1}^2 $

### **Bayesian Inference**

- Use PyMC3 to define priors and likelihoods.
- Example:

  ```python
  import pymc3 as pm

  with pm.Model() as model:
      mu = pm.Normal('mu', mu=0, sigma=1)
      sigma = pm.HalfNormal('sigma', sigma=1)
      y = pm.Normal('y', mu=mu, sigma=sigma, observed=data)
      trace = pm.sample(1000)
  ```

---

## **Assumptions and Limitations**

- **Assumptions**:
  - The time series is stationary after differencing (for ARIMA models).
  - Key events are accurately identified and dated.
- **Limitations**:
  - Dependence on the quality of the dataset (e.g., missing or noisy data).
  - Simplified assumptions in statistical models may not fully capture real-world complexities.

---

## **Expected Outputs**

- A clear understanding of the data and its characteristics.
- Familiarity with time series models (ARIMA, GARCH) and Bayesian inference.
- Identification of key events and their potential impact on oil prices.
- Documentation of assumptions, limitations, and expected outputs.
