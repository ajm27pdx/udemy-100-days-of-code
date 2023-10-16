import requests
from auth import TEQUILA_API_KEY

TEQUILA_ENDPOINT = 'https://api.tequila.kiwi.com'


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name)-> str:
        headers = {'apikey': TEQUILA_API_KEY}
        query = {'term': city_name, 'location_types': 'city'}
        response = requests.get(url='https://api.tequila.kiwi.com/locations/query', headers=headers, params=query)
        if response.json()['locations']:
            code = response.json()['locations'][0]['code']
            return code
        else:
            return 'city not found'

    def find_flights(self, departure_city, destination_city):
        headers = {'apikey': TEQUILA_API_KEY}
        query = {
            'fly_from': departure_city,
            'fly_to': destination_city,
            'date_from': '05/07/2023',
            'date_to': '14/07/2023',
            'nights_in_dst_from': 4,
            'nights_in_dst_to': 8,
            'max_stopovers': 0,
            'curr': 'USD',
            'limit': 5
        }
        response = requests.get(url=f'{TEQUILA_ENDPOINT}/v2/search', headers=headers, params=query)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city}.")
            return None

        print(data)


