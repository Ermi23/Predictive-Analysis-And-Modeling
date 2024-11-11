import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose

class EDA:
    def __init__(self, data):
        self.data = data
    
    def calculate_volatility(self, df):
        """Calculate daily returns and rolling volatility."""
        df['Daily_Return'] = df['Close'].pct_change()
        df['Rolling_Volatility'] = df['Daily_Return'].rolling(window=20).std()
        return df
    
    def plot_closing_prices(self):
        """Plot the closing prices for each ticker."""
        plt.figure(figsize=(10,6))
        for ticker, df in self.data.items():
            plt.plot(df['Date'], df['Close'], label=f'{ticker} Closing Price')
        plt.title('Stock Closing Prices (TSLA, BND, SPY)')
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.legend()
        plt.show()
    
    def decompose_time_series(self, df, ticker):
        """Decompose the time series data into trend, seasonal, and residual components."""
        ts = df.set_index('Date')['Close']
        
        # Fill missing values
        ts = ts.fillna(method='ffill').fillna(method='bfill')
        
        # Ensure 'ts' is a Series
        if not isinstance(ts, pd.Series):
            raise TypeError(f"Expected 'ts' to be a pandas Series, but got {type(ts)}")
        
        # Check for any remaining NaN values
        if ts.isnull().any():
            print(f"Warning: NaN values found in {ticker} after filling. Dropping remaining NaNs.")
            ts = ts.dropna()
        
        # Perform seasonal decomposition
        try:
            decomposition = seasonal_decompose(ts, model='multiplicative', period=252)  # 252 trading days in a year
            return decomposition
        except ValueError as e:
            print(f"Error decomposing time series for {ticker}: {e}")
            return None
    
    def plot_decomposition(self, decomposition, ticker):
        """Plot the decomposed components."""
        if decomposition:
            decomposition.plot()
            plt.suptitle(f'{ticker} Time Series Decomposition')
            plt.show()
