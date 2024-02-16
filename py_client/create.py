import requests

headers={'Authorization': f'Bearer 0c3335dca07b94432455c525cfc14e44f23b832b'}
endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "This field is done"
}

get_response = requests.post(endpoint, json=data, headers=headers) # HTTP Request
print(get_response.json())