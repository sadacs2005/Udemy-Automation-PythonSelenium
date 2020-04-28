import json
import requests
import jsonpath

apiURL = "https://reqres.in/api/users?page=2"

# Make a request
res = requests.get(apiURL)
print(res.text)

# Validate status code
assert res.status_code == 200

# Parse response to json format
jsonResponse = json.loads(res.text)
print(jsonResponse)

# Apply Jsonpath
jp = jsonpath.jsonpath(jsonResponse, "total")
print(jp[0])

# jp1 = jsonpath.jsonpath(jsonResponse, "data")
# print(jp1)

for val in jsonResponse['data']:
    print(val['first_name'])

# extract email id
for val in jsonResponse['data']:
    print(val['email'])



