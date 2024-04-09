from flask import Flask, render_template, request, jsonify
import yfinance as yf
from graphVisualization import train_model, display_line_plot, display_bar_plot, display_scatter_plot
from dataRetrieval import retrieve_stock_data
from predictionModel import train_model, predict_stock_price, evaluate_model
from keras.models import load_model

app = Flask(__name__, template_folder='templates', static_folder='static')

model = load_model('static/keras_model.h5')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/retrieve_stock_data')
def retrieve_stock_data_route():
    symbol = request.args.get('symbol')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    try:
        stock_data = yf.download(symbol,start_date,end_date)
    
        if not stock_data.empty:
            return jsonify(stock_data.to_dict(orient='split'))
        else:
            return jsonify({'error': 'No data available'})
    except Exception as e:
        return jsonify({'error': 'Failed to retrieve stock data. Please check the symbol and dates.'})

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        symbol = request.form['ticker-symbol']
        start_date = request.form['start-date']
        end_date = request.form['end-date']

        stock_data = retrieve_stock_data(symbol, start_date, end_date)

        if stock_data is not None:
            df = train_model(stock_data, symbol, start_date, end_date)

            line_graph = display_line_plot(df)
            bar_graph = display_bar_plot(df)
            scatter_graph = display_scatter_plot(df)

            return render_template('index.html', lineGraph=line_graph, barGraph=bar_graph, scatterGraph=scatter_graph)
        else:
            error_message = 'Failed to retrieve stock data. Please check the symbol and dates.'
            return render_template('index.html', error=error_message)

if __name__ == '__main__':
    app.run()













