# **Brent Oil Price Analysis - Tasks 1, 2, and 3**

## **Overview**

This repository contains the implementation for analyzing historical Brent oil prices and building an interactive dashboard to visualize the results. The project is divided into three tasks:

1. **Task 1**: Define the data analysis workflow and understand the models and data.
2. **Task 2**: Analyze Brent oil prices using advanced statistical and machine learning models, and explore external factors influencing oil prices.
3. **Task 3**: Develop an interactive dashboard using Flask (backend) and React (frontend) to visualize the analysis results.

The goal is to provide actionable insights into how various events and factors affect Brent oil prices.

## **Table of Contents**

1. [Dataset](#dataset)
2. [Installation](#installation)
3. [Directory Structure](#directory-structure)
4. [Data Analysis Workflow](#data-analysis-workflow)
5. [Advanced Models and External Factors](#advanced-models-and-external-factors)
6. [Interactive Dashboard](#interactive-dashboard)
7. [Assumptions and Limitations](#assumptions-and-limitations)
8. [Expected Outputs](#expected-outputs)

## **Dataset**

The dataset contains historical Brent oil prices from **May 20, 1987, to September 30, 2022**. Each record includes:

- **Date**: The date of the recorded price (formatted as `day-month-year`).
- **Price**: The price of Brent oil in USD per barrel.

### **Additional Data Sources**

To analyze external factors influencing oil prices, the following datasets are used:

- **Macroeconomic Indicators**: GDP, inflation rates, unemployment rates, exchange rates (from World Bank, IMF, OECD).
- **Technological Changes**: Adoption rates of fracking, renewable energy growth (from industry reports).
- **Political Events**: Geopolitical conflicts, trade policies, sanctions (from news APIs or government publications).

### **Data Source**

- The primary dataset is stored in the `data/` directory as `raw_data.csv`.
- Additional datasets are stored in the `data/` directory with descriptive filenames (e.g., `macroeconomic_indicators.csv`, `political_events.csv`).

## **Installation**

To set up the project locally, follow these steps:

### **Prerequisites**

- Python 3.8 or higher
- Node.js and npm (for React frontend)
- Git

### **Steps**

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/username/brent_oil_analysis.git
   cd brent_oil_analysis
   ```

2. **Install Python Dependencies**:
   Install the required Python packages using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

3. **Install Frontend Dependencies**:
   Navigate to the React frontend directory and install dependencies:

   ```bash
   cd dashboard/frontend
   npm install
   ```

4. **Run the Backend**:
   Start the Flask backend server:

   ```bash
   cd ../../dashboard/backend
   python app.py
   ```

5. **Run the Frontend**:
   In a separate terminal, start the React frontend:

   ```bash
   cd ../frontend
   npm start
   ```

6. Open your browser and navigate to `http://localhost:3000` to view the dashboard.

## **Directory Structure**

The project is organized into the following directories and files:

```
brent_oil_analysis/
│
├── data/
│   ├── raw_data.csv          # Raw Brent oil prices dataset
│   ├── processed_data.csv    # Processed dataset after cleaning
│   ├── macroeconomic_indicators.csv # Macroeconomic data
│   └── political_events.csv  # Political and regulatory data
│
├── src/
│   ├── data_preprocessing.py # Data cleaning and preprocessing
│   ├── time_series_models.py # Time series models (ARIMA, GARCH)
│   ├── bayesian_inference.py # Bayesian modeling using PyMC3
│   ├── feature_engineering.py # Feature engineering for advanced models
│   ├── model_training.py     # Training advanced models (LSTM, VAR, etc.)
│   └── api_endpoints.py      # Flask API endpoints for serving data
│
├── utils/
│   ├── data_utils.py         # Functions for data-related operations
│   ├── visualization_utils.py # Functions for plotting and visualizations
│   └── error_handling.py     # Error handling utilities
│
├── dashboard/
│   ├── backend/
│   │   └── app.py            # Flask backend for serving API data
│   └── frontend/
│       ├── public/           # Static assets for React app
│       ├── src/
│       │   ├── components/
│       │   │   ├── OilPriceChart.js # Component for oil price visualization
│       │   │   └── EventHighlight.js # Component for highlighting events
│       │   ├── App.js        # Main React app component
│       │   └── index.js      # Entry point for React app
│       └── package.json      # React app dependencies
│
├── main.py                   # Main script to execute the workflow
└── README.md                 # Project overview and instructions
```

## **Data Analysis Workflow**

The workflow for analyzing Brent oil prices is structured as follows:

### **1. Data Loading and Exploration**

- Load the dataset (`data/raw_data.csv`) into a Pandas DataFrame.
- Perform exploratory data analysis (EDA) to understand trends, seasonality, and anomalies.
- Visualize the time series using Matplotlib or Seaborn.

### **2. Data Preprocessing**

- Handle missing values and outliers.
- Convert the `Date` column to a datetime format.
- Merge additional datasets (e.g., macroeconomic indicators, political events).

### **3. Statistical Modeling**

- Implement time series models such as ARIMA and GARCH using `statsmodels`.
- Evaluate model performance using metrics like RMSE, MAE, and AIC/BIC.

### **4. Advanced Models**

- Train advanced models like LSTM, VAR, and Markov-Switching ARIMA.
- Use machine learning techniques to capture complex patterns and dependencies.

### **5. Bayesian Inference**

- Use PyMC3 to perform Bayesian modeling.
- Define prior distributions for parameters and estimate posterior distributions using MCMC.

### **6. Event Analysis**

- Identify key events (e.g., OPEC meetings, geopolitical conflicts) and their dates.
- Analyze price changes around these events using statistical tests (e.g., t-tests, ANOVA).

## **Advanced Models and External Factors**

### **Time Series Models**

- **ARIMA**: Captures trends and seasonality in the data.
- **GARCH**: Models volatility clustering in financial time series.
- **VAR**: Analyzes multivariate time series relationships.
- **Markov-Switching ARIMA**: Captures regime-switching behavior.

### **Machine Learning Models**

- **LSTM**: Captures long-term dependencies in sequential data.
- **Random Forests**: Identifies important features affecting oil prices.

### **External Factors**

- **Macroeconomic Indicators**: GDP, inflation, unemployment, exchange rates.
- **Technological Changes**: Fracking adoption, renewable energy growth.
- **Political Events**: Sanctions, trade policies, geopolitical conflicts.

## **Interactive Dashboard**

The dashboard allows users to interactively explore the analysis results:

- **Historical Trends**: Visualize Brent oil prices over time.
- **Event Highlight**: Highlight specific events and their impact on prices.
- **Filters**: Filter data by date range, event type, or variable.
- **Performance Metrics**: Display RMSE, MAE, and other evaluation metrics.

### **Backend**

- Built using Flask to serve API endpoints for data and predictions.

### **Frontend**

- Built using React with interactive visualizations powered by `recharts`.

## **Assumptions and Limitations**

- **Assumptions**:
  - The time series is stationary after differencing (for ARIMA models).
  - Key events are accurately identified and dated.
- **Limitations**:
  - Dependence on the quality of the dataset (e.g., missing or noisy data).
  - Simplified assumptions in statistical models may not fully capture real-world complexities.

## **Expected Outputs**

- A clear understanding of the data and its characteristics.
- Insights into how external factors influence oil prices.
- A robust interactive dashboard for stakeholders to explore the analysis results.
- Documentation of assumptions, limitations, and expected outputs.
