import json
import os
import requests

USERNAME = os.getenv("USERNAME")
IP = os.getenv("IP")
URL = f"http://{IP}/api/{USERNAME}/lights/1/state"

request_body = {
    "on": True,
    "bri": 254,
    "sat": 0
}

requests.put(URL, data=json.dumps(request_body))
