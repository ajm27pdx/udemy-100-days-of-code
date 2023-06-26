import requests
from datetime import datetime
from auth import TOKEN
USERNAME = 'ajm27pdx'
GRAPH_ID = 'graph1'
pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
headers = {
    'X-USER-TOKEN': TOKEN
}
graph_config = {
    'id': GRAPH_ID,
    'name': 'Coding Graph',
    'unit': 'min',
    'type': 'int',
    'color': 'ajisai'
}
# # Create Graph
# requests.post(url=graph_endpoint, json=graph_config, headers=headers)

date = f'{datetime.today().strftime("%Y%m%d")}'

graph_update = {
    'quantity': '45'
}


response = requests.put(url=f'{graph_endpoint}/{GRAPH_ID}/{date}', headers=headers, json=graph_update)
print(response.text)

