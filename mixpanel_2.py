#!flask/bin/python
import requests
from mixpanel import Mixpanel
import 

url = 'http://api.mixpanel.com/track/'

headers = {'Mixpanel' : 'TOKEN', 'Accept' : 'application/json', 'Content-Type' : 'application/json'}

payload = {
  "userId": "user1",
  "event": "Product Viewed",
  "properties": {
    "product_id": "pr_507f1f77bcf86cd799439011",
    "sku": "G-32",
    "category": "Games",
    "name": "Monopoly: 3rd Edition",
    "brand": "Hasbro",
    "variant": "200 pieces",
    "price": 18.99,
    "quantity": 1
  }
}

r = requests.post(url, data=payload)
print(r.text)
