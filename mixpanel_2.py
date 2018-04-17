import requests, base64, json

####3 pieces to the puzzle
#### pass the headers with the Mixpanel token
#### encode the payload
#### send encoded payload through a POST request to the HTTP API endpoint

##Mixpanel HTTP API
url = 'http://api.mixpanel.com/track/'
token = 'INSERT HERE'
headers = {'token' : token, 'Content-Type' : 'application/json'}

payload = {
  "userId": "user1",
  "event": "Product Viewed",
  "properties": {
    "product_id": "pr_507f1f77bcf86cd799439011",
    "distinct_id" : 'user1',
    "sku": "G-32",
    "category": "Games",
    "name": "Monopoly: 3rd Edition",
    "brand": "Hasbro",
    "variant": "200 pieces",
    "price": 18.99,
    "quantity": 1,
    "token" : token
  }
}

#convert dict to a string so it can be encoded
payload_json = json.dumps(payload)
print(payload_json)

#encode the payload and print
encoded_data = base64.b64encode(payload_json)
print("Here is the encoded payload: " + encoded_data)

#Connect the final URL and POST
r = requests.post(url + '?data=' + encoded_data, headers = headers)
if r.text == 1:
    print("Success your POST has been sent to mixpanel!")
else:
    print("Mixpanel returned an error")
