import requests

server_name = "https://api.github.com/"

r = requests.get(server_name + "repos/mn236/BME547/branches") # BME547AssignmentsFall2021

print(r)
print(type(r))
print(r.status_code)
print(r.text)

branches = r.json()
print(branches)
for branch in branches:
    print(branch["name"])
    
