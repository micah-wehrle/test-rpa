import requests
import time
import json

update_url = 'https://ng-proj-2-default-rtdb.firebaseio.com/test.json'

data = {
  'type': type,
  'now': time.time()
}

converted_data = json.dumps(data)

r = requests.post(url=update_url, data=converted_data)

print(r.json())