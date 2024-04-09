# #  dataRetrieval.py
# import requests
# import pandas as pd

# def retrieve_stock_data(symbol, start_date, end_date):
#     url = f"https://query1.finance.yahoo.com/v7/finance/download/{symbol}?period1={start_date}&period2={end_date}&interval=1d&events=history"
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.text
#         df = pd.read_csv(pd.compat.StringIO(data))
#         df.set_index('Date', inplace=True)
#         return df
#     else:
#         return None


import yfinance as yf

def retrieve_stock_data(symbol, start_date, end_date):
    try:
        stock_data = yf.download(symbol, start=start_date, end=end_date)
        return stock_data
    except Exception as e:
        print(f"Error retrieving stock data: {e}")
        return None
