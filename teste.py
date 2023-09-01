import base64
import json

data = {
  "skipHumanReview": True,
  "inlineDocument": {
    "mimeType": "application/pdf",
    "content": None
  }
}

_authorization = "Bearer apagado"

with open('small.pdf', 'rb') as file:
    binary_data = file.read()

base64_data = base64.b64encode(binary_data)

data['inlineDocument']['content'] = base64_data.decode('utf-8')

import requests

url = "https://us-documentai.googleapis.com/v1/projects/286362658457/locations/us/processors/be352832bca42589:process"

response = requests.post(url, data=json.dumps(data), headers={
    'Authorization': _authorization,
    'Content-Type': 'application/json; charset=utf-8'
})

print(response.json())

