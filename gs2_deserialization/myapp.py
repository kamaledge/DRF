import requests
import json

URL = "http://127.0.0.1:8000/stucreate/"

data = {
    'name': 'Rahul',
    'roll': 102,
    'city': 'Ranchi'
}

json_data = json.dumps(data) # 'dumps' convert data from python to json, for reverse thing, we use 'loads'

r = requests.post(url=URL, data=json_data)
data = r.json()
print(data)
