from flask import Flask, request, jsonify
from flask_socketio import SocketIO
from flask_swagger_ui import get_swaggerui_blueprint
from marketdataloader import MarketDataLoader
from toolkit import *
import time
import threading
import inspect
import ast
import datetime as dt

class UnsafeDependenciesError(Exception):
    """ Raised when the user custom trading analytics function's imported dependencies are deemed unsafe. """
    pass

class NonJsonSerializableError(Exception):
    """ Raised when the output of the user custom trading analytics function is not json serializable. """
    pass

def function_checker(func: str) -> None:
    """ Checks for unsafe dependencies inside a user custom function. """
    # Whitelist of unsafe dependencies
    unsafe_modules = {'os', 'sys', 'subprocess', 'ctypes'}
    # Parse the function's AST
    tree = ast.parse(func)
    # Traverse the AST and look for import statements within the function definition
    for node in ast.walk(tree):
        # Checking for imports
        if isinstance(node, ast.Import):
            for alias in node.names:
                # Checking for unsafe modules 
                if alias.name in unsafe_modules:
                    # Raise an error if the module is deemed unsafe
                    raise UnsafeDependenciesError(f"Unsafe import: please remove {alias.name} "\
                                                  "from the function's definition")
        # Checking for from imports 
        elif isinstance(node, ast.ImportFrom):
            if node.module in unsafe_modules:
                raise UnsafeDependenciesError(f"Unsafe import: imports from {node.module} "\
                                              "are not allowed, please remove it from "\
                                                "the function's definition")

def results_checker(result: any) -> None:
    """ Checks for the validity of the user custom analysis function output. """
    allowed_obj = [dict, list, tuple, str, int, float, bool, None] # List of json serializable objects
    # Checking for the output type
    if not type(result) in allowed_obj:
        # Raise an error if the output type is not json serializable
        raise NonJsonSerializableError(f'{type(result)} is not json serializable, '\
                                       'please refactor the output format to an allowed type '\
                                       f'such as {allowed_obj}')
    
def find_timedelta(freq: str) -> dict[str, int]:
    """ Returns the correct dt.timedelta argument based on the frequency provided. """
    # The maximum number of datapoints that can be retrieved through a single request
    lag = 500
    # Frequency conversion table
    table = {
        '1d': 'days',
        '1h': 'hours',
        '1m': 'minutes'
    }
    # Returning the kwargs inside a dictionnary
    return {
        table[freq]: lag
    }
    
swagger_url = '/api/v1/swagger' # API docs endpoint
api_url = '/static/swagger.json' # Swagger config file location

# Define the blueprint for swagger API documentation
swagger_blueprint = get_swaggerui_blueprint(
    base_url=swagger_url,
    api_url=api_url,
    config={
        'app_name': 'Trading Analytics API' 
    }
)
# Define the app instance
app = Flask(__name__)
# Define the websocket service
socketio = SocketIO(app)
# Register the swagger blueprint
app.register_blueprint(blueprint=swagger_blueprint, url_prefix=swagger_url)

@app.route('/api/v1/ta/sma', methods=['GET'])
def sma():
    """ Handles the simple moving average GET request. """
    try:
        # Gathering tickers inside a list
        tickers = [
            ticker.strip() for ticker in request.args['tickers'].split(',')
            if ticker.strip() # To skip missplaced commas
        ]
        # Gathering ohlcv endpoints inside a list
        ohlcv = [
            endpoint.strip() for endpoint in request.args['ohlcv'].split(',')
            if endpoint.strip()
        ]
        # Retrieving data frequency interval, if not passed through the request set it to daily
        freq = request.args.get('freq', default='1d')
        # Retrieving the starting date
        start_date = dt.datetime.strptime(
            request.args['start_date'], '%d-%m-%Y'
        )
        # Retrieving the ending date
        end_date = dt.datetime.strptime(
            request.args['end_date'], '%d-%m-%Y'
        )
        # Retrieving the moving average's rolling window lenght, if not passed through the request set it to 20
        n = int(request.args.get('n', default=20))
        # Initializing the market data loading tool
        dl = MarketDataLoader(tickers, ohlcv, freq, start_date, end_date)
        # Retrieving data
        data = dl.get_candlesticks()
        # Applying the simple moving average function
        results = simple_moving_average(data, tickers, ohlcv, n)
        # Outputing results through a json file linked to the "output" key
        return jsonify({'output': results}), 200
    # Checking for errors while retrieving market data or applying the function
    except Exception as e:
        # Returning error details through a json file linked to the "error" key
        return jsonify({'error': str(e)}), 400
    
@socketio.on(message='sma')
def handle_sma_request(data: dict[str, any]):
    """ Handles the simple moving average websocket request. """
    def send_sma_response():
        """ Sends the simple moving average latest results every minute. """
        try:
            while True:
                # Define the last data point as today
                end_date = dt.datetime.today()
                # Define the first data point based on the data frequency provided 
                start_date = end_date - dt.timedelta(**find_timedelta(freq))
                # Initializing the market data loading tool 
                dl = MarketDataLoader(tickers, ohlcv, freq=freq, start_date=start_date, end_date=end_date)
                # Retrieving data
                prices = dl.get_candlesticks()
                # Selecting the latest result of the applied simple moving average function
                results = simple_moving_average(prices, tickers, ohlcv, n)[-1]
                # Switching from timestamps to strings to avoid conversion errors
                results['Time'] = dt.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                # Sending back results to the client 
                socketio.emit('sma_response', {'output': results})
                # Sleeping for a minute
                time.sleep(60)
        except Exception as e:
            socketio.emit('sma_response', {'error': str(e)})
    try:
        # Retrieving sent tickers
        tickers = data['tickers']
        # Retrieving sent ohlcv endpoints
        ohlcv = data['ohlcv']
        # Retrieving sent data frequency, default value: '1d'
        freq = data.get('freq', '1d')
        # Retrieving the moving average's rolling window lenght, if not passed through the request set it to 20
        n = int(data.get('n', 20))
        # Creating a thread for the sma response function
        thread = threading.Thread(target=send_sma_response)
        # Starting the thread
        thread.start()
    # Checking for errors while the connection is up
    except Exception as e:
        # Sending error details to the client
        socketio.emit('sma_response', {'error': str(e)})

@app.route('/api/v1/ta/ema', methods=['GET'])
def ema():
    """ Handles the exponential moving average GET request. """
    try:
        # Gathering tickers inside a list
        tickers = [
            ticker.strip() for ticker in request.args['tickers'].split(',')
            if ticker.strip() # To skip missplaced commas
        ]
        # Gathering ohlcv endpoints inside a list
        ohlcv = [
            endpoint.strip() for endpoint in request.args['ohlcv'].split(',')
            if endpoint.strip()
        ]
        # Retrieving data frequency interval, if not passed through the request set it to daily
        freq = request.args.get('freq', default='1d')
        # Retrieving the starting date
        start_date = dt.datetime.strptime(
            request.args['start_date'], '%d-%m-%Y'
        )
        # Retrieving the ending date
        end_date = dt.datetime.strptime(
            request.args['end_date'], '%d-%m-%Y'
        )
        # Retrieving the moving average's rolling window lenght, if not passed through the request set it to 20
        n = int(request.args.get('n', default=20))
        # Initializing the market data loading tool
        dl = MarketDataLoader(tickers, ohlcv, freq, start_date, end_date)
        # Retrieving data
        data = dl.get_candlesticks()
        # Applying the exponential moving average function
        results = exponential_moving_average(data, tickers, ohlcv, n)
        # Outputing results through a json file linked to the "output" key
        return jsonify({'output': results}), 200
    # Checking for errors while retrieving market data or applying the function
    except Exception as e:
        # Returning error details through a json file linked to the "error" key
        return jsonify({'error': str(e)}), 400

@socketio.on(message='ema')
def handle_ema_request(data: dict[str, any]):
    """ Handles the exponential moving average websocket request. """
    def send_ema_response():
        """ Sends the exponential moving average latest results every minute. """
        try:
            while True:
                # Define the last data point as today
                end_date = dt.datetime.today()
                # Define the first data point based on the data frequency provided 
                start_date = end_date - dt.timedelta(**find_timedelta(freq))
                # Initializing the market data loading tool
                dl = MarketDataLoader(tickers, ohlcv, freq=freq, start_date=start_date, end_date=end_date)
                # Retrieving data
                prices = dl.get_candlesticks()
                # Selecting the latest result of the applied exponential moving average function
                results = exponential_moving_average(prices, tickers, ohlcv, n)[-1]
                # Switching from timestamps to strings to avoid conversion errors
                results['Time'] = dt.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                # Sending back results to the client 
                socketio.emit('ema_response', {'output': results})
                # Sleeping for a minute
                time.sleep(60)
        except Exception as e:
            socketio.emit('ema_response', {'error': str(e)})
    try:
        # Retrieving sent tickers
        tickers = data['tickers']
        # Retrieving sent ohlcv endpoints
        ohlcv = data['ohlcv']
        # Retrieving sent data frequency, default value: '1d'
        freq = data.get('freq', '1d')
        # Retrieving the moving average's rolling window lenght, if not passed through the request set it to 20
        n = int(data.get('n', 20))
        # Creating a thread for the ema response function
        thread = threading.Thread(target=send_ema_response)
        # Starting the thread
        thread.start()
    # Checking for errors while the connection is up
    except Exception as e:
        # Sending error details to the client
        socketio.emit('ema_response', {'error': str(e)})   
    
@app.route('/api/v1/ta/macd', methods=['GET'])
def macd():
    """ Handles the moving average convergence divergence GET request. """
    try:
        # Gathering tickers inside a list
        tickers = [
            ticker.strip() for ticker in request.args['tickers'].split(',')
            if ticker.strip() # To skip missplaced commas
        ]
        # Define needed endpoints for macd computation
        ohlcv = ['Close']
        # Retrieving data frequency interval, if not passed through the request set it to daily
        freq = request.args.get('freq', default='1d')
        # Retrieving the starting date
        start_date = dt.datetime.strptime(
            request.args['start_date'], '%d-%m-%Y'
        )
        # Retrieving the ending date
        end_date = dt.datetime.strptime(
            request.args['end_date'], '%d-%m-%Y'
        )
        # Initializing the market data loading tool
        dl = MarketDataLoader(tickers, ohlcv, freq, start_date, end_date)
        # Retrieving market data
        data = dl.get_candlesticks()
        # Applying the macd function
        results = moving_average_convergence_divergence(data, tickers)
        # Outputing results through a json file linked to the "output" key
        return jsonify({'output': results}), 200
    # Checking for errors while retrieving market data or applying the function
    except Exception as e:
        # Returning error details through a json file linked to the "error" key
        return jsonify({'error': str(e)}), 400
    
@socketio.on(message='macd')
def handle_macd_request(data: dict[str, any]):
    """ Handles the moving average convergence divergence websocket request. """
    def send_macd_response():
        """ Sends the moving average convergence divergence latest results every minute. """
        try:
            while True:
                # Define the last data point as today
                end_date = dt.datetime.today()
                # Define the first data point based on the data frequency provided  
                start_date = end_date - dt.timedelta(**find_timedelta(freq))
                # Initializing the market data loading tool 
                dl = MarketDataLoader(tickers, ohlcv, freq=freq, start_date=start_date, end_date=end_date)
                # Retrieving data
                prices = dl.get_candlesticks()
                # Selecting the latest result of the applied macd function
                results = moving_average_convergence_divergence(prices, tickers)[-1]
                # Switching from timestamps to strings to avoid conversion errors
                results['Time'] = dt.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                # Sending back results to the client 
                socketio.emit('macd_response', {'output': results})
                # Sleeping for a minute
                time.sleep(60)
        except Exception as e:
            socketio.emit('macd_response', {'error': str(e)})
    try:
        # Retrieving sent tickers
        tickers = data['tickers']
        # Retrieving closing prices
        ohlcv = ['Close']
        # Retrieving sent data frequency, default value: '1d'
        freq = data.get('freq', '1d')
        # Creating a thread for the macd response function
        thread = threading.Thread(target=send_macd_response)
        # Starting the thread
        thread.start()
    # Checking for errors while the connection is up
    except Exception as e:
        # Sending error details to the client
        socketio.emit('macd_response', {'error': str(e)})  

@app.route('/api/v1/ta/rsi', methods=['GET'])
def rsi():
    """ Handles the relative strenght index GET request. """
    try:
        # Gathering tickers inside a list
        tickers = [
            ticker.strip() for ticker in request.args['tickers'].split(',')
            if ticker.strip() # To skip missplaced commas
        ]
        # Define needed endpoints for rsi computation
        ohlcv = ['Close']
        # Retrieving data frequency interval, if not passed through the request set it to daily
        freq = request.args.get('freq', default='1d')
        # Retrieving the starting date
        start_date = dt.datetime.strptime(
            request.args['start_date'], '%d-%m-%Y'
        )
        # Retrieving the ending date
        end_date = dt.datetime.strptime(
            request.args['end_date'], '%d-%m-%Y'
        )
        # Retrieving the moving average's rolling window lenght, if not passed through the request set it to 20
        n = int(request.args.get('n', default=20))
        # Initializing the market data loading tool
        dl = MarketDataLoader(tickers, ohlcv, freq, start_date, end_date)
        # Retrieving market data
        data = dl.get_candlesticks()
        # Applying the rsi function
        results = relative_strenght_index(data, tickers, n)
        # Outputing results through a json file linked to the "output" key
        return jsonify({'output': results}), 200
    # Checking for errors while retrieving market data or applying the function
    except Exception as e:
        # Returning error details through a json file linked to the "error" key
        return jsonify({'error': str(e)}), 400
    
@socketio.on(message='rsi')
def handle_rsi_request(data: dict[str, any]):
    """ Handles the relative strenght index websocket request. """
    def send_rsi_response():
        """ Sends the relative strenght index latest results every minute. """
        try:
            while True:
                # Define the last data point as today
                end_date = dt.datetime.today()
                # Define the first data point based on the data frequency provided  
                start_date = end_date - dt.timedelta(**find_timedelta(freq))
                # Initializing the market data loading tool
                dl = MarketDataLoader(tickers, ohlcv, freq=freq, start_date=start_date, end_date=end_date)
                # Retrieving data
                prices = dl.get_candlesticks()
                # Selecting the latest result of the applied rsi function
                results = relative_strenght_index(prices, tickers, n)[-1]
                # Switching from timestamps to strings to avoid conversion errors
                results['Time'] = dt.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                # Sending back results to the client 
                socketio.emit('rsi_response', {'output': results})
                # Sleeping for a minute
                time.sleep(60)
        except Exception as e:
            socketio.emit('rsi_response', {'error': str(e)})
    try:
        # Retrieving sent tickers
        tickers = data['tickers']
        # Retrieving closing prices
        ohlcv = ['Close']
        # Retrieving sent data frequency, default value: '1d'
        freq = data.get('freq', '1d')
        # Retrieving the moving average's rolling window lenght, if not passed through the request set it to 20
        n = int(data.get('n', 20))
        # Creating a thread for the rsi response function
        thread = threading.Thread(target=send_rsi_response)
        # Starting the thread
        thread.start()
    # Checking for errors while the connection is up
    except Exception as e:
        # Sending error details to the client
        socketio.emit('rsi_response', {'error': str(e)})  

@app.route('/api/v1/ta/bbands', methods=['GET'])
def bbands():
    """ Handles the bollinger bands GET request. """
    try:
        # Gathering tickers inside a list
        tickers = [
            ticker.strip() for ticker in request.args['tickers'].split(',')
            if ticker.strip() # To skip missplaced commas
        ]
        # Define needed endpoints for bollinger bands computation
        ohlcv = ['Low', 'High', 'Close']
        # Retrieving data frequency interval, if not passed through the request set it to daily
        freq = request.args.get('freq', default='1d')
        # Retrieving the starting date
        start_date = dt.datetime.strptime(
            request.args['start_date'], '%d-%m-%Y'
        )
        # Retrieving the ending date
        end_date = dt.datetime.strptime(
            request.args['end_date'], '%d-%m-%Y'
        )
        # Retrieving the moving average's rolling window lenght, if not passed through the request set it to 20
        n = int(request.args.get('n', default=20))
        # Retrieving the number of standard deviations used to compute upper and lower bands, if not passed through the request set it to 2
        m = int(request.args.get('m', default=2))
        # Initializing the market data loading tool
        dl = MarketDataLoader(tickers, ohlcv, freq, start_date, end_date)
        # Retrieving market data
        data = dl.get_candlesticks()
        # Applying the bollinger bands function
        results = bollinger_bands(data, tickers, n, m)
        # Outputing results through a json file linked to the "output" key
        return jsonify({'output': results}), 200
    # Checking for errors while retrieving market data or applying the function
    except Exception as e:
        # Returning error details through a json file linked to the "error" key
        return jsonify({'error': str(e)}), 400
    
@socketio.on(message='bbands')
def handle_bbands_request(data: dict[str, any]):
    """ Handles the bollinger bands websocket request. """
    def send_bbands_response():
        """ Sends the bollinger bands latest results every minute. """
        try:
            while True:
                # Define the last data point as today
                end_date = dt.datetime.today()
                # Define the first data point based on the data frequency provided  
                start_date = end_date - dt.timedelta(**find_timedelta(freq))
                # Initializing the market data loading tool
                dl = MarketDataLoader(tickers, ohlcv, freq=freq, start_date=start_date, end_date=end_date)
                # Retrieving data
                prices = dl.get_candlesticks()
                # Selecting the latest result of the applied bbands function
                results = bollinger_bands(prices, tickers, n, m)[-1]
                # Switching from timestamps to strings to avoid conversion errors
                results['Time'] = dt.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                # Sending back results to the client 
                socketio.emit('bbands_response', {'output': results})
                # Sleeping for a minute
                time.sleep(60)
        except Exception as e:
            socketio.emit('bbands_response', {'error': str(e)})
    try:
        # Retrieving sent tickers
        tickers = data['tickers']
        # Retrieving closing prices
        ohlcv = ['Low', 'High', 'Close']
        # Retrieving sent data frequency, default value: '1d'
        freq = data.get('freq', '1d')
        # Retrieving the moving average's rolling window lenght, if not passed through the request set it to 20
        n = int(data.get('n', 20))
        # Retrieving the number of standard deviations used to compute upper and lower bands, if not passed through the request set it to 2
        m = int(data.get('m', 2))
        # Creating a thread for the bbands response function
        thread = threading.Thread(target=send_bbands_response)
        # Starting the thread
        thread.start()
    # Checking for errors while the connection is up
    except Exception as e:
        # Sending error details to the client
        socketio.emit('bbands_response', {'error': str(e)}) 
    
@app.route('/api/v1/custom/submit', methods=['POST'])
def submit():
    """ Handles the user custom trading analytics function POST request. """
    try:
        # Collecting the posted function
        fb64 = request.json['func']
        # Converting the function back to its original form
        func = b642func(fb64)
        # Collecting the market data loading tool's options
        options = request.json['options']
        # Collecting the function's keyword arguments, if not passed by the client set it to an empty dict
        kwargs = request.json.get('kwargs', {})
        # Reading individual data loading parameters
        tickers = options['tickers'] # Tickers list
        ohlcv = options['ohlcv'] # Ohlcv endpoints list
        freq = options['freq'] # Data frequency
        start_date = dt.datetime.fromtimestamp(options['start_date']) # Starting date
        end_date = dt.datetime.fromtimestamp(options['end_date']) # Ending date
        # Checking for unsafe dependencies inside the posted function
        function_checker(inspect.getsource(func))
        # Initializing the tool
        dl = MarketDataLoader(tickers, ohlcv, freq, start_date, end_date)
        # Retreiving data
        data = dl.get_candlesticks()
        # Applying the user custom function
        results = func(data, **kwargs)
        # Checking for the output validity before returning the results to the user
        results_checker(results)
        # Outputing results inside a json file with the 'output' key
        return jsonify({'output': results}), 200
        # Checking for errors while retrieving market data, applying the user function or returning results
    except Exception as e:
        # Returning the error details inside a json file with the 'error' key
        return jsonify({'error': str(e)}), 400
    
if __name__ == '__main__':
    socketio.run(app)