import requests

#endpoint = "https://httpbin.org/status/200/"
#endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint, data={"query": "Hello World!"}) # HTTP Request
print(get_response.json()['message']) # print raw text responsecls