import requests

server_name = "http://vcm-7631.vm.duke.edu:5002/"

request_json = {"Recipient": "<ID1>",
                "Donor": "ID2"
                }
r = requests.get(server_name + "get_patients/mn236", json=request_json)
print(r.text)

r = requests.get(server_name + "get_blood_type/F4", json=request_json)
print(r.text)

r = requests.get(server_name + "get_blood_type/F7", json=request_json)
print(r.text)

request_json = {"Name": "mn236", "Match": "No"}
r = requests.post(server_name + "match_check", json=request_json)
print(r.text)
