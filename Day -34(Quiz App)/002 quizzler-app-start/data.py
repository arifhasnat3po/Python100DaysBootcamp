import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(
    url="https://opentdb.com/api.php?amount=10&type=boolean", params=parameters)
response.raise_for_status()
data = response.json()

response_code = data["response_code"]

if response_code == 0:
    # Success, you can access the results
    question_data = data["results"]
else:
    # Handle the case where response_code is not 0
    print(f"Error: Response code is not 0. Actual code: {response_code}")
