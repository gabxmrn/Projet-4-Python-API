import pandas as pd

"""
This file shows how a user can build his own trading analytics python3 function.
When creating a custom function, make sure to apply the following rules to ensure valid execution:

    - The function's first argument should always be the DataFrame containing retrieved market data.  
    - Import needed dependencies inside the function's definition to ensure their presence on the server side.
    - Always define secondary helper functions inside the main function's definition.
    - If the custom function returns multiple results, make sure to return them inside a json serializable object such as 
      dictionnaries, lists, tuples ...  
    - Do not attempt to return numpy ndarray or pandas DataFrame objects as it will raise an error while attempting to send
      back results. Make sure to convert them to valid objects beforehand by using methods as df.to_dict(orient='records').

Please refer to our client.py file to check how a user can send its custom function to our API.
"""

# User custom trading analytics function
def stochastic_oscillator(data: pd.DataFrame, tickers: list[str], k_periods: int, d_periods: int) -> list[dict[str, float]]:
    """ Computes the stochastic oscillator for a set of crypto-assets tickers. """
    # Make sure to import the needed dependencies inside of the main function
    import pandas as pd
    # Results DataFrame
    results = pd.DataFrame()
    # Looping through tickers
    for ticker in tickers:
        # Computing the rolling k periods max high prices (highest highs)
        high_max = data[f'{ticker}-High'].rolling(window=k_periods, min_periods=k_periods).max()
        # Computing the rolling k periods min low prices (lowest lows)
        low_min = data[f'{ticker}-Low'].rolling(window=k_periods, min_periods=k_periods).min()
        # Computing the %k fast line as a percentage of the difference between highest highs and lowest lows
        k = pd.Series(
            (data[f'{ticker}-Close'] - low_min) * 100 / (high_max - low_min),
            name=f'{ticker}-%K'
        )
        # Computing the %d simple moving average of the fast line to smooth relative pricing
        d = pd.Series(
           k.rolling(window=d_periods, min_periods=d_periods).mean(),
           name=f'{ticker}-%D'
        )
        # Aggregating the computed Series into the results DataFrame
        results = pd.concat([results, k, d], axis=1)
    # Adding candlestick opening dates then dropping NaN's
    results = pd.concat([data['Time'], results], axis=1).dropna()
    # Returning the results DataFrame as a dict 
    return results.to_dict(orient='records')

