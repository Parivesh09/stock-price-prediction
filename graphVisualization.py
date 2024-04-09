import matplotlib.pyplot as plt
import io
import base64
from dataRetrieval import retrieve_stock_data

def train_model(symbol, start_date, end_date):

    stock_data = retrieve_stock_data(symbol, start_date, end_date)
    print(stock_data.head())

    df = stock_data.copy()
    return df

def display_line_plot(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df['Date'], df['Close'], label='Stock Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Stock Price Trend - Line Plot')
    plt.legend()
    plt.grid(True)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()

    graph_image = base64.b64encode(buffer.getvalue()).decode()
    return graph_image

def display_bar_plot(df):
    plt.figure(figsize=(10, 6))
    plt.bar(df['Date'], df['Volume'], label='Volume')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.title('Stock Volume - Bar Plot')
    plt.legend()
    plt.grid(True)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()

    graph_image = base64.b64encode(buffer.getvalue()).decode()
    return graph_image

def display_scatter_plot(df):
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Date'], df['Open'], label='Opening Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Stock Opening Price - Scatter Plot')
    plt.legend()
    plt.grid(True)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()

    graph_image = base64.b64encode(buffer.getvalue()).decode()
    return graph_image
