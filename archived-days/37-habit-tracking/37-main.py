import requests
from datetime import datetime
from auth import TOKEN
USERNAME = 'ajm27pdx'
GRAPH_ID = 'graph2'
pixela_endpoint = 'https://pixe.la/v1/users'

headers = {
    'X-USER-TOKEN': TOKEN
}

# # Create User
# user_params = {
#     'token': TOKEN,
#     'username': USERNAME,
#     'agreeTermsOfService': 'yes',
#     'notMinor': 'yes'
# }
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# # Create Graph
graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'


# # Create Graph
# graph_config = {
#     'name': 'OreSatTime',
#     'unit': 'hrs',
#     'type': 'int',
#     'color': 'kuro'
# }
# response = requests.put(url=f'{graph_endpoint}/{GRAPH_ID}', json=graph_config, headers=headers)
# print(response.text)


date = f'{datetime.today().strftime("%Y%m%d")}'

# # Add Pixel
new_pixel = {
    'date': date,
    'quantity': '1',
    'optionalData': '{\"task\":\"attended meeting\"}'
}
response = requests.post(url=f'{graph_endpoint}/{GRAPH_ID}', headers=headers, json=new_pixel)
print(response.text)


# # Update Pixel
# graph_update = {
#     'quantity': '45'
# }
# response = requests.put(url=f'{graph_endpoint}/{GRAPH_ID}/{date}', headers=headers, json=graph_update)
# print(response.text)

