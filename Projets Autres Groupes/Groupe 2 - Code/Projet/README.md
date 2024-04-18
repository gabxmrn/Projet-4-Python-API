# Trading Analytics API

Master 272 - Economics and Financial Engineering - Year 2023/2024 - Project n°2

## Authors

Audrey Teyssier, Axelle Roques, Briac Bonnin, Christian Buciulica, Jean-Baptiste Del Rio, Lucas Ducrocq.

## Overview

The Trading Analytics API provides a wide range of Technical Analysis Indicators applied to Crypto-Assets Markets. It also allows users to submit and apply their own custom Python 3 Analytics Functions to historical and real-time data.

We are providing users with a service of basic technical analysis indicators applied to crypto markets such as `moving average convergence divergence`, `relative strenght index`, `bollinger bands` ...
For more informations please checkout our swagger documentation endpoint on `api/v1/swagger`.

!["Swagger documentation snippet"](static/swagger.png)

The main feature of our application is the submission and application of customized functions to real-time and historical market data.
The following subsections will aim at giving you all the technical details needed to successfully send your first request.

## Requirements

To run this project you will need the following software installed on your system:

- **Programming Language**: Python (version 3.8 or higher)

- **Libraries**: `aiohttp`, `dill`, `flask`, `flask_socketio`, `flask_swagger_ui`, `pandas`, `python-socketio`, `requests`

To install all needed dependencies make sure to run the following command line: ``` pip install requirements.txt ```

## Getting Started

### API's url

To start off, once the app is running the custom function submission endpoint will be hosted on the following url:

```python
url = 'http://127.0.0.1:5000/api/v1/custom/submit'
```

### Building a trading analytics function

When writing your custom Python 3 function make sure to apply the following rules to ensure valid execution:

- The function's first argument should always be the `DataFrame` containing retrieved market data.  
- Import needed dependencies inside the function's definition to ensure their presence on the server side.
- Always define secondary helper functions inside the main function's definition.
- If the custom function returns multiple results, make sure to return them inside a `json` serializable object such as `dictionnaries`, `lists`, `tuples` ...  
- Do not attempt to return `numpy ndarray` or `pandas DataFrame` objects as it will raise an error while attempting to send back results. Make sure to convert them to valid objects beforehand by using methods as `df.to_dict(orient='records')`.

Here is a quick example of a well written function:

```python
def stochastic_oscillator(data: pd.DataFrame, tickers: list[str], k_periods: int, d_periods: int) -> list[dict[str, float]]:
    """ Computes the stochastic oscillator for a  set of crypto-assets tickers. """
    import pandas as pd
    
    "your code goes here" 

    return results.to_dict(orient='records')
```

### Selecting market data

To apply your function to market data please provide the following parameters:

- `tickers`: List of tickers to retrieve (with USDT as quote asset) e.g. `BTCUSDT`, `ETHUSDT`, ...
- `ohlcv`: List of market data endpoints to retrieve e.g. `Open`, `High`, `Low`, `Close` or `Volume`
- `freq`: The interval between data points e.g. `1d`, `1h`, ...
- `start_date`: The first data point to retrieve (pass it as a timestamp to avoid any errors)
- `end_date`: The last data point to retrieve (pass it as a timestamp to avoid any errors)

Once selected, gather all parameters inside a `dict` object with keys as described above.

Here is an example on how to select market data using python:

```python
tickers = ['BTCUSDT', 'ETHUSDT', 'SOLUSDT'] 
ohlcv = ['Low', 'High', 'Close'] 
freq = '1d' 
end_date = dt.datetime.today() 
start_date = end_date - dt.timedelta(days=365) 

options = {
    'tickers': tickers,
    'ohlcv': ohlcv, 
    'freq': freq,
    'start_date': int(start_date.timestamp()),
    'end_date': int(end_date.timestamp())
}
```

### Serializing and sending the function

Posting your custom function to our API will require you to serialize as a `base64 string` beforehand. To do so, use our helper function `func2b64` available in the `toolkit.py` file. If your function takes arguments (other than the market data table) as inputs, make sure to gather them inside a `dict` with keys named as in the function's definition.

Apply the following example to correctly serialize your function:

```python
kwargs = {
    'tickers': tickers,
    'k_periods': 14,
    'd_periods': 3 
}

fb64 = func2b64(stochastic_oscillator)
```

Once done, the last required step is to gather all three objects inside a main `dict` in order to post it as `json` to our API.

```python
params = {
    'func': fb64, 
    'kwargs': kwargs, 
    'options': options 
}
response = requests.post(url, json=params)
```

### Retrieving results

The applied function's results will be send back to the user as a `json` object with one of the following keys as indicator:

- `output`: Successful operation e.g. code 200
- `error`: Invalid request e.g. code 400

```python
details = response.json()
```

All the provided code is available for testing in our `example.py` and `client.py` files.

## Websockets

Our API also offers a websocket service for the basic technical analysis indicators mentioned on the `api/v1/swagger` endpoint.

The emit messages are the following:

- `sma` for Simple Moving Average
- `ema` for Exponential Moving Average
- `macd` for Moving Average Convergence Divergence
- `rsi` for Relative Strenght Index
- `bbands` for Bollinger Bands

The responses are formulated as `indicator name` + `_response` e.g. `bbands_response`

Every minute the server will send to the client the latest value of the indicator based on the tickers and parameters provided.

Here is a quick demonstration on how to get set up:

### Importing the socketio client

To use our service you will need to import the `socketio` library and define an instance of the client.

```python
import socketio
client = socketio.Client()
```

### Handling server responses

To handle server responses you need to define a handler function wrapped with the `@client.on` decorator.
Make sure to correctly spell the response name as described above.

```python
@client.on('bbands_response')
def on_bbands_response(data: dict[str, any]) -> None:
    print(data)
```

For this simple example we only print the received data each time it is sent by the server.

### Establishing connection and sending a request

To send a request you will need to establish a connection to the socket's url.

```python
client.connect('http://127.0.0.1:5000/')
```

After defining the needed tickers and parameters, send the request using the client's `emit` method with the correct message and wait for the server's responses using the client's `wait` method.

```python
data = {
    'tickers': ['BTCUSDT', 'ETHUSDT'],
    'freq': '1h',
    'n': 24,
    'm': 2
}
client.emit('bbands', data)
client.wait()
```
