import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv("DEVICES_CONTROL_URL")
govee_api_key = os.getenv("GOVEE_API_KEY")
device_mac = os.getenv("GOVEE_DEVICE_MAC_ADDRESS")
device_model = os.getenv("GOVEE_DEVICE_MODEL")

white_value = {"r": 255, "g": 255, "b": 255}
red_value = {"r": 255, "g": 0, "b": 0}
green_value = {"r": 0, "g": 255, "b": 0}
blue_value = {"r": 0, "g": 0, "b": 255}
warm_white_value = {"r": 255, "g": 146, "b": 39}
black_value = {"r": 0, "g": 0, "b": 0}

headers = {
    "Content-Type": "application/json",
    "Govee-API-Key": govee_api_key
}

data = {
    "device": device_mac,
    "model": device_model,
    "cmd": {
        "name": "color",
        "value": warm_white_value
    }
}

response = requests.put(url, headers=headers, data=json.dumps(data))

print(response.status_code)
print(response.json())
