import requests
from datetime import datetime

USERNAME = "arifhasnat"
TOKEN = "jhfldkajshlfkjhaslkajdshf"
GRAPHID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Reading Books",
    "unit": "page",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(
#     url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


graph_endpoint_post = f"{graph_endpoint}/{GRAPHID}"

# today = datetime(year=2023, month=12, day=6)
# # print(today)
today = datetime.now()
formatted_date = today.strftime("%Y%m%d")
print(formatted_date)

post_configuration = {
    "date": formatted_date,
    "quantity": input("How many pages did you read today?"),

}

update_pixel_data = f"{graph_endpoint_post}/{formatted_date}"

response = requests.post(
    url=graph_endpoint_post, json=post_configuration, headers=headers

)
# print(response.text)

# update_pixel_data_params = {
#     # "date": formatted_date,
#     "quantity": "20"
# }

# response = requests.put(
#     url=update_pixel_data, json=update_pixel_data_params, headers=headers

# )
# print(response.text)
