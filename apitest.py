import requests
import urllib3
import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


r = requests.get('https://api.github.com/events')
print (r)

response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code)
jprint(response.json())
