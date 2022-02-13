import cv2
import requests
import base64
import json
import os

print("Take Duck Photo: Hit 's'")
video_capture = cv2.VideoCapture(0)
while True:
    ret, frame = video_capture.read()
    cv2.imshow("Video", frame)

    if cv2.waitKey(1)& 0xFF == ord('s'):
        cv2.imwrite("duck.png", frame)
        break

print("Take First Photo: Hit 's'")
while True:
    ret, frame = video_capture.read()
    cv2.imshow("Video", frame)

    if cv2.waitKey(1)& 0xFF == ord('s'):
        cv2.imwrite("person.png", frame)
        break

cwd = os.getcwd()

base = "http://127.0.0.1:5000/getImage"

image_file2 = cwd + '/duck.png'
image_file = cwd + '/person.png'

with open(image_file, "rb") as f:
    im_bytes = f.read()        
im_b64 = base64.b64encode(im_bytes).decode("utf8")

with open(image_file2, 'rb') as y:
    im_bytes2 = y.read()
im_b642 = base64.b64encode(im_bytes2).decode("utf8")

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
  
payload = json.dumps({"face": im_b64, "duck": im_b642})


response = requests.post(base, data=payload, headers=headers)
try:
    #data = response.json()
    print("Worked")
except requests.exceptions.RequestException:
    print(response.text)