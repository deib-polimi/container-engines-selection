import json
import requests
import time

import sys

url = sys.argv[1]
name = sys.argv[2]

headers={'Accept':'application/vnd.github.v3.text-match+json'}

page=1
items = []
while True:
    resp = requests.get (f'{url}&page={page}', headers=headers)
    data = resp.json()
    time.sleep(5)
    print(data)
    if 'items' not in data or not data['items']:
        break
    items += data['items']
    page += 1

res = {"query" : url, 'items' : items}

data = json.dumps(res, indent=4)

with open(name, 'w') as outfile:
    outfile.write(data)