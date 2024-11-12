# Stock Price Forecasting and Portfolio Optimization

This project implements a time series forecasting model for Tesla (TSLA), Vanguard Total Bond Market ETF (BND), and S&P 500 ETF (SPY) using LSTM (Long Short-Term Memory) neural networks. The project aims to forecast future stock prices and optimize a sample portfolio based on these forecasts. The tasks are broken into four key stages, each covered by notebooks and scripts in the project.

## Table of Contents
- [Project Structure](#project-structure)
- [Setup and Requirements](#setup-and-requirements)
- [Tasks Overview](#tasks-overview)
  - [Task 1: Data Preparation](#task-1-data-preparation)
  - [Task 2: Time Series Forecasting](#task-2-time-series-forecasting)
  - [Task 3: Forecast Market Trends](#task-3-forecast-market-trends)
  - [Task 4: Portfolio Optimization](#task-4-portfolio-optimization)
- [How to Run](#how-to-run)
- [Project Components](#project-components)

---

## Project Structure

```
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows
│       └── unittests.yml
├── Data/
│   ├── raw/
│   │   └── [ticker].csv         # Raw data files (e.g., TSLA.csv, BND.csv, SPY.csv)
│   ├── processed/
│   │   ├── [ticker]_train.csv    # Training data for each ticker
│   │   ├── [ticker]_test.csv     # Test data for each ticker
│   │   └── [ticker]_forecast.csv # Forecast data for each ticker (generated in Task 3)
├── Models/
│   └── [ticker]_lstm_model.h5    # Saved LSTM models for each ticker (generated in Task 2)
├── notebooks/
│   ├── Task_2_Time_Series_Forecasting.ipynb
│   ├── Task_3_Forecasting_Market_Trends.ipynb
│   └── Task_4_Portfolio_Optimization.ipynb
├── scripts/
│   └── [script files].py
├── tests/
│   └── [test scripts].py
├── requirements.txt
└── README.md
```

- **Data/raw/**: Contains the initial raw data CSV files for each ticker.
- **Data/processed/**: Holds processed data files for training/testing and forecasted values.
- **Models/**: Contains trained LSTM model files for each ticker.
- **notebooks/**: Contains Jupyter notebooks for each task.
- **scripts/**: Folder for reusable Python scripts.
- **tests/**: Folder for unit tests.

---

## Setup and Requirements

### Prerequisites
- Python 3.7+
- Required Python packages listed in `requirements.txt`

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Ermi23/Stock-Price-Forecasting-and-Portfolio-Optimization.git
   cd stock-forecasting-and-optimization
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Tasks Overview

### Task 1: Data Preparation
The initial data preparation step (handled within the `notebooks/Task_2_Time_Series_Forecasting.ipynb` notebook) involves:
- Loading historical stock price data from `Data/raw/`.
- Processing and splitting the data into training and testing sets.
- Saving processed data into `Data/processed/`.

### Task 2: Time Series Forecasting
This task trains an LSTM model for each ticker to forecast future prices:
- `notebooks/Task_2_Time_Series_Forecasting.ipynb` trains the LSTM models for `TSLA`, `BND`, and `SPY`.
- Models are saved in the `Models/` folder for each ticker.
- Evaluation metrics (MAE, RMSE, MAPE) are calculated and printed.

### Task 3: Forecast Market Trends
This task generates and analyzes the forecasted stock prices:
- Forecasts future prices for 6–12 months using the trained LSTM models.
- Saves forecasted data for each ticker as `<ticker>_forecast.csv` in `Data/processed/`.
- `notebooks/Task_3_Forecasting_Market_Trends.ipynb` visualizes the forecast alongside historical data and provides a trend analysis.

### Task 4: Portfolio Optimization
In this final task, a sample portfolio is optimized based on forecasted stock prices:
- Uses forecast data to compute expected returns, volatility, and Sharpe Ratio.
- Optimizes portfolio weights to maximize the Sharpe Ratio.
- Analyzes the portfolio's risk and return profile.
- Results and performance are visualized in `notebooks/Task_4_Portfolio_Optimization.ipynb`.

---

## How to Run

Each task is contained within its respective Jupyter notebook under the `notebooks/` folder. Follow these steps to complete the project:

1. **Run Task 2 Notebook** (`Task_2_Time_Series_Forecasting.ipynb`):
   - This trains and saves the LSTM models for each ticker in the `Models/` folder.
   
2. **Run Task 3 Notebook** (`Task_3_Forecasting_Market_Trends.ipynb`):
   - Generates and saves forecast data for each ticker in `Data/processed/`.
   
3. **Run Task 4 Notebook** (`Task_4_Portfolio_Optimization.ipynb`):
   - Loads forecasted data and optimizes the portfolio based on forecasted returns.

---

## Project Components

### Notebooks
Each notebook is designed to be self-contained, guiding you through the steps and outputs with explanations and visualizations.

- **Task_2_Time_Series_Forecasting.ipynb**: LSTM model training and evaluation for time series forecasting.
- **Task_3_Forecasting_Market_Trends.ipynb**: Forecast generation, visualization, and trend analysis.
- **Task_4_Portfolio_Optimization.ipynb**: Portfolio optimization based on forecasted stock price trends.

### Scripts
- **scripts/**: Add custom scripts here if you plan to modularize any part of the notebooks for reuse or scaling up.

### Tests
- **tests/**: Includes unit tests to validate model outputs, data processing functions, and evaluation metrics.

---

## Summary

This project provides a comprehensive approach to stock price forecasting and portfolio optimization. By forecasting future stock prices and adjusting portfolio weights accordingly, you can leverage predictive insights for better-informed investment strategies.

Feel free to contribute by adding more assets, experimenting with different forecasting models, or extending the portfolio optimization strategy. For questions or feedback, please reach out or open an issue on GitHub.

--- 