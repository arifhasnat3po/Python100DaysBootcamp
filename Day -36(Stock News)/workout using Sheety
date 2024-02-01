import requests
from datetime import datetime

GENDER = "Male"
WEIGHT_KG = 65
HEIGHT_CM = 175.26
AGE = 24

CHATGPT_API = "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"
NUTRITIONIX_API = "6584630ed3b2a0971568250d7ddeddee"
NUTRITIONIX_APP_ID = "827d6ebf"

nutriton_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercises you did: ")

sheety_url = "https://api.sheety.co/611a7e903063ee271bd1eb81591de0a1/workoutTracking/workouts"


headers = {
    'Content-Type': 'application/json',
    'x-app-id': NUTRITIONIX_APP_ID,
    'x-app-key': NUTRITIONIX_API,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response = requests.post(
    url=nutriton_url, json=parameters, headers=headers
)

result = response.json()
# print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# print(today_date)
# print(now_time)
for exercise in result["exercises"]:
    sheety_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "calories": exercise["nf_calories"],
            "duration": exercise["duration_min"],
        }
    }

    bearer_headers = {
        "Authorization": "Bearer 9847yfhsdaiojboasyfdj"
    }
    sheet_response = requests.post(
        sheety_url, json=sheety_inputs, headers=bearer_headers)

    print(sheet_response.text)
