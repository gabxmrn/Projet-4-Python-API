import asyncio
import aiohttp
import pandas as pd
import datetime as dt

class TickerError(Exception):
    """ Raised when an exception is caught while retrieving data for a univariate ticker. """
    pass

class OhlcvError(Exception):
    """ Raised when a user's specified ohlcv endpoint is not featured on Binance's API. """
    pass

class MarketDataLoader:
    """
    Market data loading tool for crypto-assets ohlcv candlesticks powered by Binance's API.

    Note
    ----------
    The results are returned in a DataFrame object including a `"Time"` column which contains the candlesticks opening times.
    The other columns will be named following the ticker-ohlcv format e.g. `"SOLUSDT-Close"`, `"XRPUSDT-High"`, ... 

    Attributes
    ----------
    tickers: list[str]
        The list of tickers to retrieve (with USDT as quote asset) e.g. `"BTCUSDT"`, `"ETHUSDT"`, ... 
    ohlcv: list[str]
        The list of market data endpoints to retreive e.g. `"Open"`, `"High"`, `"Low"`, `"Close"` or `"Volume"`.
    freq: str
        The interval between data points e.g. `"1d"`, `"1h"`, `"1m"`, ...
    start_date: datetime
        The first data point to retrieve with datetime format.
    end_date: datetime
        The last data point to retrieve with datetime format.
    cross_ref: dict[str, int]
        Dictionary of Binance's API compatible ohlcv endpoints as keys and their associated json index as value. 

    Public Methods
    ----------
    get_candlsticks(self) -> DataFrame:
        Gathers ohlcv endpoints for the specified tickers, dates and frequency within a limit of 500 points.
    
    Private Methods
    ----------
    fetch_candlesticks(self, session: aiohttp.ClientSession, ticker: str) -> DataFrame:
        Fetches ohlcv candlestick data for a univariate ticker between specified dates.
    gather_candlesticks(self) -> DataFrame:
        Gathers ohlcv candlestick data for all specified tickers using async API calls. 

    Raises
    ----------
    TickerError:
        Raises error if an exception is caught while retrieving data for a univariate ticker.
    OhlcvError:
        Raises error if a user's specified ohlcv endpoint is not featured on Binance's API.
    """
    def __init__(self, tickers: list[str], ohlcv: list[str], freq: str,
                 start_date: dt.datetime, end_date: dt.datetime) -> None:
        """
        Initializes the market data loading tool by providing lists of tickers, ohlcv endpoints, starting and ending dates.

        Parameters
        ----------      
        tickers: list[str]
            The list of tickers to retrieve (with USDT as quote asset) e.g. `"BTCUSDT"`, `"ETHUSDT"`, ... 
        ohlcv: list[str]
            The list of market data endpoints to retreive e.g. `"Open"`, `"High"`, `"Low"`, `"Close"` or `"Volume"`.
        freq: str
            The interval between data points e.g. `"1d"`, `"1h"`, `"1m"`, ...
        start_date: datetime
            The first data point to retrieve with datetime format.
        end_date: datetime
            The last data point to retrieve with datetime format.

        Raises
        ----------      
        OhlcvError:
            Raises error if a user's specified ohlcv endpoint is not featured on Binance's API.
        """
        self.tickers = tickers
        self.ohlcv = ohlcv
        self.freq = freq
        self.start_date = start_date
        self.end_date = end_date
        # Dictionary of compatible ohlcv endpoints and their associated json index
        self.__cross_ref = {
            'Time': 0, # Candlestick opening timestamp
            'Open': 1,
            'High': 2,
            'Low': 3,
            'Close': 4,
            'Volume': 5
        }
        # Checking for the validity of user inputed endpoints
        for endpoint in self.ohlcv:
            if not endpoint in self.__cross_ref:
                # Raise OhlcvError in case of incorrect endpoint
                raise OhlcvError(f'{endpoint} incorrect for ohlcv endpoint, '\
                                 'value should either be "Open", "High", "Low", '\
                                    '"Close" or "Volume".')
            
    async def __fetch_candlesticks(self, session: aiohttp.ClientSession, ticker: str) -> pd.DataFrame:
        """
        Fetches ohlcv candlestick data for a univariate ticker between specified dates.

        Returns
        ----------      
        DataFrame:
            DataFrame of ohlcv data for an univariate ticker with associated candlestick opening times as index.

        Raises
        ----------      
        TickerError:
            Raises error if an exception is caught while retrieving data for a univariate ticker.
        """
        url = 'https://api.binance.com/api/v3/klines' # Binance's API base url
        # Dictionary of parameters transfered to the API
        params = {
            'symbol': ticker,
            'interval': self.freq,
            'startTime': int(self.start_date.timestamp() * 1_000), 
            'endTime': int(self.end_date.timestamp() * 1_000) # Converting dates to timestamps to match the API's expected format
        }
        # Sending async get requests to the API
        async with session.get(url, params=params) as response:
            details = await response.json() # Awaiting for results as json
            try:
                time = [
                    dt.datetime.fromtimestamp(ts[self.__cross_ref['Time']] / 1_000)
                    for ts in details # Collecting candlesticks opening timestamps and converting them to datetime format 
                ]
                values = {
                    f'{ticker}-{key}': [data[self.__cross_ref[key]] for data in details]
                    for key in self.ohlcv # Collecting ohlcv data inside a dictionary with ticker-ohlcv as key 
                }
                # Returning collected results as a DataFrame with opening times as index
                return pd.DataFrame(values, index=time).astype(float)
            # Raising TickerError in case of a thrown exception while collecting data
            except Exception:
                raise TickerError('Error encountered when retreiving data for '\
                                  f'ticker: {ticker}')
            
    async def __gather_candlesticks(self) -> pd.DataFrame:
        """
        Gathers ohlcv candlestick data for all specified tickers using async API calls. 

        Returns
        ----------     
        DataFrame:
             DataFrame of gathered ohlcv data with associated candlestick opening times.
        """
        async with aiohttp.ClientSession() as session:
            tasks = [
                self.__fetch_candlesticks(session, ticker) 
                for ticker in self.tickers # Creating separate tasks for single tickers
                ]
            results = await asyncio.gather(*tasks) # Awating for all results to be returned
        # Returning collected results inside a single DataFrame with opening times as first column 
        return pd.concat(results, axis=1).reset_index(names='Time')
    
    def get_candlesticks(self) -> pd.DataFrame:
        """
        Gathers ohlcv endpoints for the specified tickers, dates and frequency within a limit of 500 points.
        
        Returns
        ----------     
        DataFrame:
             DataFrame of gathered ohlcv data including a `"Time"` column containing candlesticks opening times
             with the other columns being named following the ticker-ohlcv format e.g. `"SOLUSDT-Close"`, `"XRPUSDT-High"`, ... 
        """
        return asyncio.run(self.__gather_candlesticks())
   
if __name__ == '__main__':
    pass