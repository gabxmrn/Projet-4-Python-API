import pandas as pd

"""
This file shows an example of a user custom made trading analytics function.
When creating a custom function, one should apply to the following rules:

    - The function's first argument always has to be a DataFrame containing the retrieved market data.  
    - Import needed packages inside the function's definition to ensure their presence on the server side.
    - If needed, define auxiliary functions inside the function's definition to ensure their presence on the server side.
    - If the function returns multiple results, make sure to return them inside a dictionary. If the output format is a 
      DataFrame, use the method .to_dict(orient='records').
    - Do not attempt to return non json serializable objects as it will raise an error when attempting to send back results.

To see how a user can send its custom trading analytics function to our API, please check the client.py file.
"""

# Example n°1: returning multiple results inside a dict using an auxiliary helper function
def stats_desc(data: pd.DataFrame, tickers: list[str]) -> dict:
    """
    Computes descriptive statistics on returns for a set of given tickers. 

    Arguments
    ----------
    data: DataFrame
        A DataFrame of Closing prices for one or multiple assets.
    tickers: list[str]
        The list of tickers for which the statistics will be computed.

    Returns
    ----------
    dict:
        A dictionnary of descriptive statistics (mean, std, min, max) for each ticker, 
        including the variance-covariance matrix of returns
    """
    import numpy as np # For now the user has to import the used packages inside its custom function

    # Always define the auxiliary helper function inside of the main one
    def log_return(data: pd.DataFrame, lag: int) -> pd.DataFrame:
        """ Computes log returns for a given dataset of asset prices and a lag level. """
        # Extracting only asset prices from the DataFrame
        prices = data.loc[:, ~data.columns.isin(['Time', 'Volume'])]
        # Returning the log returns DataFrame excluding nan's
        return np.log(prices / prices.shift(lag)).dropna()
    
    # Results dictionnary
    results = {}
    # Computing log returns with one period lag
    returns = log_return(data, lag=1)
    # Looping through specified tickers
    for ticker in tickers:
        # Computing the average return
        results[f'{ticker}-mean'] = np.mean(returns[f'{ticker}-Close'])
        # Computing the standard deviation of returns 
        results[f'{ticker}-std'] = np.std(returns[f'{ticker}-Close'])
        # Retrieving the max return over the period
        results[f'{ticker}-min'] = np.min(returns[f'{ticker}-Close']) 
        # Retrieving the min return over the period
        results[f'{ticker}-max'] = np.max(returns[f'{ticker}-Close'])
    # Computing the variance-covariance matrix of returns 
    results['VCV'] = returns.cov().to_dict(orient='records') # Converting the DataFrame to a dict for serialization purposes

    return results

# Example n°2: returning a DataFrame as a dict
def bollinger_bands(data: pd.DataFrame, tickers: list[str], n: int, m: int) -> dict[str, list[float]]:
    """
    Computes Bollinger Bands for a set of given tickers and parameters.

    Arguments
    ----------
    data: DataFrame
        A DataFrame of High, Low and Closing prices for one or multiple assets.
    tickers: list[str]
        The list of tickers for which the trendlines will be computed.
    n: int
        The moving average's rolling window.
    m: int
        The number of standard deviations away from the moving average used when computing the upper and lower bounds.

    Returns
    ----------
    dict[str, list[float]]:
        Dictionary containing the Bollinger Bands for each ticker and date. 
    """
    import pandas as pd 
    # Results DataFrame
    results = pd.DataFrame() 
    # Looping through specified tickers
    for ticker in tickers:
        # Computing the typical price as the average of low, high and closing prices
        tp = (data[f'{ticker}-Low'] + data[f'{ticker}-High'] + data[f'{ticker}-Close']) / 3
        # Computing the n periods moving average
        ma = pd.Series(tp.rolling(window=n, min_periods=n).mean(), name=f'{ticker}-Ma')
        # Computing the n periods rolling standard deviation 
        sigma = tp.rolling(window=n, min_periods=n).std()
        # Computing the upper-bound of the bollinger band
        upper_bound = pd.Series(ma + m * sigma, name=f'{ticker}-Ub')
        # Computing the lower-bound of the bollinger band
        lower_bound = pd.Series(ma - m * sigma, name=f'{ticker}-Lb')
        # Aggregating the computed series into the results DataFrame
        results = pd.concat([results, lower_bound, ma, upper_bound], axis=1)
    # Adding candlestick opening dates then dropping NaN's
    results = pd.concat([data['Time'], results], axis=1).dropna()
    # Returning the results DataFrame as a dict 
    return results.to_dict(orient='records')