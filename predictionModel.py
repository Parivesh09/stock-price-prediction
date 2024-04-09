# predictionModel.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from dataRetrieval import retrieve_stock_data
from keras.models import load_model

def train_model(stock_data, symbol, start_date, end_date):
    df = stock_data.copy() 

    df.dropna(inplace=True)
    df['Date'] = pd.to_datetime(df['Date'])

    df['Log_Returns'] = np.log(df['Adj Close'] / df['Adj Close'].shift(1))

    scaler = StandardScaler()
    df['Scaled_Feature'] = scaler.fit_transform(df['Feature'].values.reshape(-1, 1))

    selected_features = ['Open', 'High', 'Low', 'Volume']

    y = df['Close']

    X = df[selected_features]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = load_model('static/keras_model.h5')
    return model

def predict_stock_price(model, stock_data):
    df = stock_data.copy() 

    selected_features = ['Open', 'High', 'Low', 'Volume']
    y = df['Close']
    X = df[selected_features]

    predictions = model.predict(X)

    return predictions

def evaluate_model(model, stock_data):
    df = stock_data.copy() 

    selected_features = ['Open', 'High', 'Low', 'Volume']
    y = df['Close']
    X = df[selected_features]
    predictions = model.predict(X)
    mse = mean_squared_error(y, predictions)
    accuracy = 1 - mse / y.var()

    return accuracy
