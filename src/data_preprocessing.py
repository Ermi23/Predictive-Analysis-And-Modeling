import yfinance as yf
import pandas as pd

class FinancialDataProcessor:
    def __init__(self, tickers, start_date, end_date):
        self.tickers = tickers
        self.start_date = start_date
        self.end_date = end_date
        self.data = {}
    
    def load_data(self):
        """Load stock data from Yahoo Finance for each ticker."""
        for ticker in self.tickers:
            self.data[ticker] = self._download_data(ticker)
        return self.data
    
    def _download_data(self, ticker):
        """Download stock data for a given ticker."""
        stock_data = yf.download(ticker, start=self.start_date, end=self.end_date)
        stock_data['Ticker'] = ticker
        return stock_data
    
    def clean_data(self):
        """Clean the stock data by handling missing values for each ticker."""
        for ticker, df in self.data.items():
            if df.isnull().sum().sum() > 0:
                df.fillna(method='ffill', inplace=True)
                df.fillna(method='bfill', inplace=True)
            df['Date'] = df.index  # Ensure 'Date' is a column
            self.data[ticker] = df
        return self.data
