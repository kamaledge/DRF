import requests
import json


URL = 'http://127.0.0.1:8000/studentapi/' # never forget the last slash


# GET METHOD to read
def get_data(id = None):
    data = {}
    if id:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data= json_data) # request for data, response is stored in r
    # print(r)
    data = r.json() # extracting response data, received from request, returns json-encoded content of the response
    print(data)
    
# get_data(2)


# POST method for INSERT

def post_data():
    data = {
        'name': 'Sonal',
        'roll': 108,
        'city': 'Dhanbad'
    }

    json_data = json.dumps(data)

    r = requests.post(url=URL, data= json_data) # request for data, response is stored in r
    # print(r)
    data = r.json() # extracting response data, received from request, returns json-encoded content of the response
    print(data)

# post_data()


# PUT METHOD for Partial Update
def update_data():
    data = {
        'id': 7,
        'name': 'Rohit',
        # 'roll': 105, # uncomment when Patial is False in studentserializer in the view
        'city': 'Tata'
    }

    json_data = json.dumps(data)

    # PUT method for partial update
    r = requests.put(url=URL, data= json_data) # request for data, response is stored in r
    # print(r)
    data = r.json() # extracting response data, received from request, returns json-encoded content of the response
    print(data)

# update_data()


# DELETE method for delete
def delete_data():
    data = {'id': 7}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)

delete_data()

