from auth import newsapi_key
from datetime import date, timedelta
import requests


def get_news(query: str):
    newsapi_endpoint = 'https://newsapi.org/v2/everything'
    yst_date = date.today() - timedelta(days=1)
    yst_fmt = yst_date.strftime('%Y-%m-%d')

    parameters = {
        'apiKey': newsapi_key,
        'q': query,
        'from': yst_fmt,
        'language': 'en',
        'searchin': 'title',
        'domains': 'marketwatch.com,barrons.com,biztoc.com',
        'sortBy': 'popularity'
    }
    response = requests.get(newsapi_endpoint, params=parameters)
    response.raise_for_status()
    return response.json()
