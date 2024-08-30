import yfinance as yf
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import thing

# Function to fetch stock data


# Function to plot the stock data in CLI
def plot_stock_data(ticker):
    hist = thing.get_stock_data(ticker)
    
    plt.figure(figsize=(10, 5))
    plt.plot(hist.index, hist['Close'], label='Close Price')
    plt.title(f'Past 90 Days of {ticker}(NYSE)')
    plt.xlabel('Date')
    plt.ylabel('Price($USD)')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    ticker_symbol = input("Enter the stock ticker symbol: ")
    plot_stock_data(ticker_symbol)