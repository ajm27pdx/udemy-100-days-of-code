import requests
from datetime import date, timedelta
from auth import alphavantage_key


def get_stock_delta(symbol: str):
    alphavantage_endpoint = 'https://www.alphavantage.co/query'
    parameters = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'apikey': alphavantage_key,
    }
    response = requests.get(alphavantage_endpoint, params=parameters)
    response.raise_for_status()
    daily = response.json()['Time Series (Daily)']
    yst_date = date.today() - timedelta(days=1)
    ystyst_date = yst_date - timedelta(days=1)
    yst_fmt = yst_date.strftime('%Y-%m-%d')
    ystyst_fmt = ystyst_date.strftime('%Y-%m-%d')
    two_day_date = {yst_fmt: daily[yst_fmt],
                    ystyst_fmt: daily[ystyst_fmt]}
    delta = (float(daily[yst_fmt]['4. close']) - float(daily[ystyst_fmt]['4. close'])) / float(daily[yst_fmt]['4. close']) * 100
    # date.today()
    return delta


