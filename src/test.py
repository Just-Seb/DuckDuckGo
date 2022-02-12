import requests
import base64
import json
import os

cwd = os.getcwd()

base = "http://127.0.0.1:5000/getImage""

image_file = cwd + '/type_of_ducks/HarlequinDuck.png'

with open(image_file, "rb") as f:
    im_bytes = f.read()        
im_b64 = base64.b64encode(im_bytes).decode("utf8")

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
  
payload = json.dumps({"image": im_b64, "other_key": "value"})
response = requests.get(base, data=payload, headers=headers)
try:
    data = response.json()     
    print(data)                
except requests.exceptions.RequestException:
    print(response.text)
