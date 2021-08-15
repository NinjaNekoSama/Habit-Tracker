import requests
import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "purushotham"
TOKEN = "dfsdsijsjdkod"

user_params = {

    "token": TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor" : "yes"
}

# response = requests.post(url = pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {

    "id" : "graph1",
    "name": "Piano Graph",
    "unit": "Hours",
    "type": "int",
    "color": "sora"
}

headers = {

    "X-USER-TOKEN" : TOKEN
}

# response = requests.post(url = graph_endpoint, json= graph_config, headers = headers)
# print(response.text)

value_endpoint = f"{graph_endpoint}/graph1"

today = datetime.datetime.now( )
# print(today)
value_params = {

    "date": today.strftime("%Y%m%d"),
    "quantity": "1"
}
# response = requests.post(url = value_endpoint, json= value_params, headers = headers)
# print(response.text)

update_endpoint = f"{value_endpoint}/{today.strftime('%Y%m%d')}"

# response = requests.put(url = update_endpoint, json=value_params,headers=headers)
# print(response.text)

response= requests.delete(url=update_endpoint, headers=headers)
print(response.text)