import requests
import json


rado = requests.get('https://api.github.com/users/radorado')
print ("radorado's users url:", rado.url, '\n')
print (rado.text, '\n')
# Getting a json from radorado's users using the python library requests
# rado_users_json is a dictionary
rado_users_json = rado.json()

# json.dumps() with parameters sort_keys=True and indent=4 serializes
# rado_users_json to a json formatted string which can be pretty
# printed on the console when calling the print method
rado_users_pprinting = json.dumps(rado_users_json, sort_keys=True, indent=4)
print (rado_users_pprinting)

# deserializing the json document rado_users_pprinting to a dictionary
# using json.loads() method
rado_users_to_dict = json.loads(rado_users_pprinting)
print (rado_users_to_dict['following'])
