"""
The following script shows an example on how to send a custom python3 function to our API.
For more informations on our GET requests offer, please checkout the api/v1/swagger endpoint.  
To ensure correct execution, make sure to respect the following guideline:

    - Serialize your custom function into a base64 string using the func2b64 helper from out toolkit.
    - Gather the function's keyword arguments (all but the market data table) inside a dictionnary.
    - Store the market data loading tool parameters inside a dictionnary with 'tickers', 'ohlcv', 'freq', 'start_date'
      and 'end_date' as keys. (Dates should be passed as timestamps to avoid any conversion errors)
    - Aggregate the objects described above inside a main dictionnary with keys 'func', 'kwargs' and 'options' associated
      to the base64 representation of the function, its keyword arguments and the loading tool's parameters respectively.

Request results are returned as application/json content with 'output' key indicating successful operation or 'error' key
indicating invalid request. 
"""

if __name__ == '__main__':

    # Importing the needed dependencies
    import requests
    import pandas as pd
    import datetime as dt
    # Importing the custom analysis function
    from example import stochastic_oscillator
    # Importing the base64 conversion helper function
    from toolkit import func2b64
    
    # Initializing the data loading tool's parameters
    tickers = ['BTCUSDT', 'ETHUSDT', 'SOLUSDT'] # List of tickers to retreive (with USDT as quote asset)
    ohlcv = ['Low', 'High', 'Close'] # Collecting Low, High and Closing prices for each ticker
    freq = '1d' # Daily price interval
    end_date = dt.datetime.today() # Setting the last data point as today
    start_date = end_date - dt.timedelta(days=365) # Starting the analysis a year prior

    # Gathering the market data loader parameters inside a dict
    options = {
        'tickers': tickers,
        'ohlcv': ohlcv, 
        'freq': freq,
        'start_date': int(start_date.timestamp()),
        'end_date': int(end_date.timestamp()) # Make sure to convert starting and ending dates to timestamps
    }

    # Dictionary storing the custom function's keyword arguments
    kwargs = {
        'tickers': tickers,
        'k_periods': 14,
        'd_periods': 3 # Make sure that the keys are labeled the same as in the function's definition
    }

    # Use the func2b64 helper function from our toolkit to convert your custom function to a base64 string
    fb64 = func2b64(stochastic_oscillator)

    # Aggregating all needed elements inside the params dict 
    params = {
        'func': fb64, # Base64 representation of the custom function
        'kwargs': kwargs, # The function's keyword arguments
        'options': options # Market data loader options
    }

    url = 'http://127.0.0.1:5000/api/v1/custom/submit' # API's url
    response = requests.post(url, json=params) # Posting the request with params as json
    details = response.json() # Retrieving results as json

    if not 'error' in details:
        # If no error occured while posting we print the function's results 
        results = pd.DataFrame.from_dict(details['output'], orient='columns') # Turning back results into their original form
        print(results)
    else:
        # Else we print the error details
        print(details)