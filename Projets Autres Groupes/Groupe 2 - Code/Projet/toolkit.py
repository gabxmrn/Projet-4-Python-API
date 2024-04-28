import dill
import base64
import pandas as pd


def b642func(fb64: str) -> callable:
    """ Converts a base64 representation of a python function back to its original form. """
    # Converting the base64 string to bytes
    fbyt = base64.b64decode(fb64)
    # Returning the original function
    return dill.loads(fbyt)


def func2b64(func: callable) -> str:
    """ Serializes a python function into a base64 string. """
    # Serializing the original function into bytes
    fbyt = dill.dumps(func)
    # Returning the base64 string version of the function
    return base64.b64encode(fbyt).decode('utf-8')


def simple_moving_average(data: pd.DataFrame, tickers: list[str], ohlcv: list[str], n: int) -> list[dict[str, float]]:
    """
    Computes the simple moving average for a set of crypto-assets ticker-ohlcv pairs.

    Arguments
    ----------
    data: DataFrame
        DataFrame of ohlcv prices for one or multiple USDT quoted crypto-assets.
    tickers: list[str]
        List of asset tickers for which the moving averages will be computed.
    ohlcv: list[str]
        List of ohlcv endpoints, associated to individual tickers, for which the moving averages will be computed.
    n: int
        Moving average's rolling window size.

    Returns
    ----------
    list[dict[str, float]]:
        List of DataFrame rows stored inside dictionnaries with column names as keys
        and simple moving average data as value.
    """
    # Results DataFrame
    results = pd.DataFrame()
    # Looping through specified tickers
    for ticker in tickers:
        # Looping through specified endpoints
        for endpoint in ohlcv:
            # Computing the n period simple moving average for the ticker-ohlcv pair
            sma = pd.Series(
                data[f'{ticker}-{endpoint}'].rolling(window=n, min_periods=n).mean(),
                name=f'{ticker}-{endpoint}-Sma'  # Series column name
            )
            # Aggregating the computed Series into the results DataFrame
            results = pd.concat([results, sma], axis=1)
    # Adding candlestick opening dates then dropping NaN's
    results = pd.concat([data['Time'], results], axis=1).dropna()
    # Returning the results DataFrame as a dict
    return results.to_dict(orient='records')


def exponential_moving_average(data: pd.DataFrame, tickers: list[str], ohlcv: list[str], n: int) -> list[
    dict[str, float]]:
    """
    Computes the exponential moving average for a set of crypto-assets ticker-ohlcv pairs.

    Arguments
    ----------
    data: DataFrame
        DataFrame of ohlcv prices for one or multiple USDT quoted crypto-assets.
    tickers: list[str]
        List of asset tickers for which the moving averages will be computed.
    ohlcv: list[str]
        List of ohlcv endpoints, associated to individual tickers, for which the moving averages will be computed.
    n: int
        Moving average's rolling window size.

    Returns
    ----------
    list[dict[str, float]]:
        List of DataFrame rows stored inside dictionnaries with column names as keys
        and exponential moving average data as value.
    """
    # Results DataFrame
    results = pd.DataFrame()
    # Looping through specified tickers
    for ticker in tickers:
        # Looping through specified endpoints
        for endpoint in ohlcv:
            # Computing the n period exponential moving average for the ticker-ohlcv pair
            ema = pd.Series(
                data[f'{ticker}-{endpoint}'].ewm(span=n, min_periods=n, adjust=False).mean(),
                name=f'{ticker}-{endpoint}-Ema'  # Series column name
            )
            # Aggregating the computed Series into the results DataFrame
            results = pd.concat([results, ema], axis=1)
    # Adding candlestick opening dates then dropping NaN's
    results = pd.concat([data['Time'], results], axis=1).dropna()
    # Returning the results DataFrame as a dict
    return results.to_dict(orient='records')


def moving_average_convergence_divergence(data: pd.DataFrame, tickers: list[str]) -> list[dict[str, float]]:
    """
    Computes the moving average convergence divergence indicator for a set of crypto-assets tickers.

    Arguments
    ----------
    data: DataFrame
        DataFrame of "Close" prices for one or multiple USDT quoted crypto-assets.
    tickers: list[str]
        List of asset tickers for which the macd will be computed.

    Returns
    ----------
    list[dict[str, float]]:
        List of DataFrame rows stored inside dictionnaries with column names as keys
        and macd data as value.
    """
    # Results DataFrame
    results = pd.DataFrame()
    # Looping through specified tickers
    for ticker in tickers:
        # Computing the short term (12 periods) exponential moving average of closing prices
        ema_12 = data[f'{ticker}-Close'].ewm(span=12, adjust=False).mean()
        # Computing the long term (26 periods) exponential moving average of closing prices
        ema_26 = data[f'{ticker}-Close'].ewm(span=26, adjust=False).mean()
        # Computing the macd
        macd = pd.Series(ema_12 - ema_26, name=f'{ticker}-Macd')
        # Computing the signal line
        signal = pd.Series(macd.ewm(span=9, adjust=False).mean(), name=f'{ticker}-Signal')
        # Aggregating the computed Series into the results DataFrame
        results = pd.concat([results, macd, signal], axis=1)
    # Adding candlestick opening dates then excluding the formation period
    results = pd.concat([data['Time'], results], axis=1).iloc[26:]
    # Returning the results DataFrame as a dict
    return results.to_dict(orient='records')


def relative_strenght_index(data: pd.DataFrame, tickers: list[str], n: int) -> list[dict[str, float]]:
    """
    Computes the relative strenght index for a set of crypto-assets tickers.

    Arguments
    ----------
    data: DataFrame
        DataFrame of "Close" prices for one or multiple USDT quoted crypto-assets.
    tickers: list[str]
        List of asset tickers for which the rsi will be computed.
    n: int
        Moving average's rolling window size.

    Returns
    ----------
    list[dict[str, float]]:
        List of DataFrame rows stored inside dictionnaries with column names as keys
        and rsi data as value.
    """
    # Results DataFrame
    results = pd.DataFrame()
    # Looping through specified tickers
    for ticker in tickers:
        # Computing the price delta
        delta = data[f'{ticker}-Close'].diff(periods=1)
        # Calculating the n period moving average of gains 
        gains = delta.where(cond=delta > 0, other=0).rolling(window=n, min_periods=n).mean()
        # Calculating the n period moving average of absolute losses
        losses = - delta.where(cond=delta < 0, other=0).rolling(window=n, min_periods=n).mean()
        # Calculating the relative strenght ratio
        rs = gains / losses
        # Calculating the relative strenght index 
        rsi = pd.Series(100 - (100 / (1 + rs)), name=f'{ticker}-Rsi')
        # Aggregating the computed Series into the results DataFrame
        results = pd.concat([results, rsi], axis=1)
    # Adding candlestick opening dates then dropping NaN's
    results = pd.concat([data['Time'], results], axis=1).dropna()
    # Returning the results DataFrame as a dict
    return results.to_dict(orient='records')


def bollinger_bands(data: pd.DataFrame, tickers: list[str], n: int, m: int) -> list[dict[str, float]]:
    """
    Computes the bollinger bands for a set of crypto-assets tickers.

    Arguments
    ----------
    data: DataFrame
        DataFrame of "Low", "High" and "Close" prices for one or multiple USDT quoted crypto-assets.
    tickers: list[str]
        List of asset tickers for which the trendlines will be computed
    n: int
        Moving average's rolling window size.
    m: int
        Number of standard deviations used when computing the band's upper and lower bounds.

    Returns
    ----------
    list[dict[str, float]]:
        List of DataFrame rows stored inside dictionnaries with column names as keys
        and bollinger bands data as value.
    """
    # Results DataFrame
    results = pd.DataFrame()
    # Looping through specified tickers
    for ticker in tickers:
        # Computing the ticker's typical price as the average of low, high and closing prices
        tp = (data[f'{ticker}-Low'] + data[f'{ticker}-High'] + data[f'{ticker}-Close']) / 3
        # Computing the ticker's n period moving average
        ma = pd.Series(tp.rolling(window=n, min_periods=n).mean(), name=f'{ticker}-Ma')
        # Computing the ticker's n period rolling standard deviation 
        sigma = tp.rolling(window=n, min_periods=n).std()
        # Computing the upper-bound of the bollinger band
        upper_bound = pd.Series(ma + m * sigma, name=f'{ticker}-Ub')
        # Computing the lower-bound of the bollinger band
        lower_bound = pd.Series(ma - m * sigma, name=f'{ticker}-Lb')
        # Aggregating the computed Series into the results DataFrame
        results = pd.concat([results, lower_bound, ma, upper_bound], axis=1)
    # Adding candlestick opening dates then dropping NaN's
    results = pd.concat([data['Time'], results], axis=1).dropna()
    # Returning the results DataFrame as a dict 
    return results.to_dict(orient='records')


if __name__ == '__main__':
    pass