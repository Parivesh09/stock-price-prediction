// script.js
document.addEventListener('DOMContentLoaded', function () {
    const predictionForm = document.getElementById('prediction-form');

    predictionForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const tickerSymbol = document.getElementById('ticker-symbol').value;
        const startDate = document.getElementById('start-date').value;
        const endDate = document.getElementById('end-date').value;

        fetch(`/retrieve_stock_data?symbol=${tickerSymbol}&start_date=${startDate}&end_date=${endDate}`)
            .then(response => response.json())
            .then(data => {
                console.log(data);
                if (data.error) {
                    alert(data.error);
                } else {
                    displayStockGraph(data);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred. Please try again later.');
            });
    });

    function displayStockGraph(data) {
        const lineGraphDiv = document.getElementById('line-graph');
        const barGraphDiv = document.getElementById('bar-graph');
        const scatterGraphDiv = document.getElementById('scatter-graph');
    
        if (!data || data.columns.length === 0 || data.data.length === 0) {
            lineGraphDiv.innerHTML = '<p>No data available</p>';
            barGraphDiv.innerHTML = '<p>No data available</p>';
            scatterGraphDiv.innerHTML = '<p>No data available</p>';
            return;
        }
    
        const dates = data.index;
        const closePrices = data['Close'];
        const highPrices = data['High'];
        const lowPrices = data['Low'];
        const volumes = data['Volume'];
    
        const lineTrace = {
            x: dates,
            y: closePrices,
            type: 'scatter',
            mode: 'lines',
            name: 'Close Prices',
            line: {
                color: 'blue',
                width: 2
            }
        };
    
        const lineLayout = {
            title: 'Stock Price Trend (Line Graph)',
            xaxis: { title: 'Date' },
            yaxis: { title: 'Price' },
            margin: { t: 30, b: 50, l: 50, r: 30 }
        };
    
        Plotly.newPlot('line-graph', [lineTrace], lineLayout);
    
        const barTrace = {
            x: dates,
            y: highPrices,
            type: 'bar',
            name: 'High Prices',
            marker: {
                color: 'green'
            }
        };
    
        const barLayout = {
            title: 'Stock Price Trend (Bar Graph)',
            xaxis: { title: 'Date' },
            yaxis: { title: 'Price' },
            margin: { t: 30, b: 50, l: 50, r: 30 }
        };
    
        Plotly.newPlot('bar-graph', [barTrace], barLayout);
    
        const scatterTrace = {
            x: dates,
            y: volumes,
            type: 'scatter',
            mode: 'markers',
            name: 'Volume',
            marker: {
                size: 8,
                color: 'red'
            }
        };
    
        const scatterLayout = {
            title: 'Stock Volume Trend (Scatter Plot)',
            xaxis: { title: 'Date' },
            yaxis: { title: 'Volume' },
            margin: { t: 30, b: 50, l: 50, r: 30 }
        };
    
        Plotly.newPlot('scatter-graph', [scatterTrace], scatterLayout);
    }
     
});

