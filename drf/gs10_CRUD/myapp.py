import requests
import json

from requests.api import head


URL = 'http://127.0.0.1:8000/studentapi/' # never forget the last slash


# GET METHOD to read
def get_data(id = None):
    data = {}
    if id:
        data = {'id': id}

    headers = {'content-Type': 'application/json'} #declaring content type
    json_data = json.dumps(data)
    r = requests.get(url=URL, headers=headers, data= json_data) # request for data, response is stored in r
    # print(r)
    data = r.json() # extracting response data, received from request, returns json-encoded content of the response
    print(data)
    
# get_data()


# POST method for INSERT

def post_data():
    data = {
        'name': 'Rai',
        'roll': 112,
        'city': 'Ranchi'
    }

    headers = {'content-Type': 'application/json'} #declaring content type
    json_data = json.dumps(data)

    r = requests.post(url=URL, headers=headers, data= json_data) # request for data, response is stored in r
    # print(r)
    data = r.json() # extracting response data, received from request, returns json-encoded content of the response

    print(data)

# post_data()


# PUT METHOD for Partial Update
def update_data():
    data = {
        'id': 5,
        'name': 'Rohit',
        # 'roll': 105, # uncomment when Patial is False in studentserializer in the view
        'city': 'Tata'
    }

    headers = {'content-Type': 'application/json'} #declaring content type
    json_data = json.dumps(data)

    # PUT method for partial update
    r = requests.put(url=URL,  headers=headers, data= json_data) # request for data, response is stored in r
    # print(r)
    data = r.json() # extracting response data, received from request, returns json-encoded content of the response
    print(data)

# update_data()


# DELETE method for delete
def delete_data():
    data = {'id': 8}
    headers = {'content-Type': 'application/json'} #declaring content type
    json_data = json.dumps(data)
    r = requests.delete(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)

delete_data()

