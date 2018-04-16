from mixpanel import Mixpanel

mp = Mixpanel('TOKEN')

#tracks text mixpanel event
mp.track("user2", "Product Viewed", {
    "product_id": "pr_507f1f77bcf86cd799439011",
    "sku": "G-32",
    "category": "Games",
    "name": "Monopoly: 3rd Edition",
    "brand": "Hasbro",
    "variant": "200 pieces",
    "price": 18.99,
    "quantity": 1
  }
)


print("Success! You did it")
