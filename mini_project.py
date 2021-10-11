import requests

server_name = "http://vcm-21170.vm.duke.edu:5000/"

request_json = {"a": 1,
                "b": 2
                }
r = requests.post(server_name + "sum", json=request_json)
