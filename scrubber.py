# install requests first
# #install pip3 


import requests

import json



#scrub takes an object and strips off PII data
def scrub(dat):
    default_mask_list = ["name", "username", "password"]
    for k in dat:
        if k in default_mask_list:
            dat[k] = "*****"
        elif k == "email":
            dat[k] = "*****" + dat[k][dat[k].find('@'):]
        elif k == "friends":
            friends = dat["friends"]
            for friend in friends:
                scrub(friend)

# connect to the unit test API server
response = requests.get("http://localhost:3001/users")

def main(response):
    data = response.json()
    #print(json_string)
    #data = {
    #    "id": 123,
    #    "name": "Elsa",
    #    "username": "xXfrozen_princessXx",
    #    "email": "elsa@arendelle.com",
    #    "age": 21,
    #    "power": "ice ray",
    #    "friends": [
    #        {
    #            "id": 234,
    #            "username": "MagicSnowman32"
    #        },
    #        {
    #            "id": 456,
    #            "username": "call_me_anna"
    #        }
    #    ]
    #}
    scrub(data)
    json_string = json.dumps(data)
    print(json_string)
    with open('json_log.json', 'w') as outfile:
         outfile.write(json_string)

if __name__ == "__main__":
    main(response)
