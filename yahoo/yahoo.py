"""
Title       : Yahoo
Description : Defines function to get data from Yahoo! Finance API.
Author      : Bernardo Paulsen
Version     : 0.1.0
"""
import datetime
import numpy                         as np
import pandas                        as pd
from   pandas_datareader import data

def get(
    ticker       : str, 
    initial_date : tuple,
    final_date   : tuple,
    log_return   : bool = True) -> pd.DataFrame:
    """
    Gets market data for individual assets from Yahoo! Finance API given stock ticker and first and last date.

    :param ticker: Ticker of stock in Yahoo Finance!
    :type ticker: str
    :param initial_date: Initial date for the series, (YYYY,M,D)
    :type initial_date: tuple
    :param final_date: Final date for the series, (YYYY,M,D)
    :type final_date: tuple
    :param log_return: Whether to calculate lgo return, defaults to True
    :type log_return: bool, optional

    :return: Market data for the asset
    :rtype: pandas.DataFrame
    """
    initial_date     = datetime.datetime(*initial_date)
    final_date       = datetime.datetime(*final_date)
    prices           = data.DataReader(ticker, "yahoo", initial_date, final_date)
    if log_return:
        prices["LogRet"] = np.log(prices["Adj Close"]/prices["Adj Close"].shift(1))
    return prices