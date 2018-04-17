import requests, base64, json

#### Segment & Mixpanel HTTP API
#### A few steps are involved:
#### 1) Implement Mixpanel token so requests are authenticated
#### 2) Setup the payload with the proper parameters
#### 3) Convert the payload from a dictionary to a json string so it can be encoded
#### 4) Encode the payload json to base64
#### 5) Build and send the the POST request with valid data parameters (url + ?data= + encoded payload) 

#Mixpanel HTTP API Endpoint
url = 'http://api.mixpanel.com/track/'
token = 'INSERT HERE'
headers = {'token' : token, 'Content-Type' : 'application/json'}

#Payload with required token
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

#convert dict to a json string so it can be encoded
payload_json = json.dumps(payload)
print(payload_json)

#encode the payload and verify
encoded_data = base64.b64encode(payload_json)
print("Here is the encoded payload: " + encoded_data)

#build the final url with data params and POST
r = requests.post(url + '?data=' + encoded_data, headers = headers)
if r.text == 1:
    print("Success your POST has been sent to mixpanel!")
else:
    print("Mixpanel returned an error")
