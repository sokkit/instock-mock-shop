from flask import Flask, jsonify

print( "running")

listings = [
    {"itemId": 1, "shopId": 1, "shopName": "Johns Business", "itemName": "Birthday Cockatoo", "liveOrders": 0, "stock": 30, "sales": 50},
    {"itemId": 2, "shopId": 1, "shopName": "Johns Business", "itemName": "Blank Koala", "liveOrders": 0, "stock": 25, "sales":53},
    {"itemId": 3, "shopId": 1, "shopName": "Johns Business", "itemName": "Birthday Crocodile", "liveOrders": 0, "stock": 33, "sales": 45},
    {"itemId": 4, "shopId": 2, "shopName": "TillyScribbles", "itemName": "Nestle Pure Life", "liveOrders": 0, "stock": 31, "sales": 40},
    {"itemId": 5, "shopId": 2, "shopName": "TillyScribbles", "itemName": "Birthday LLama", "liveOrders": 0, "stock": 10, "sales": 20},
    {"itemId": 6, "shopId": 2, "shopName": "TillyScribbles", "itemName": "Magic Avocado", "liveOrders": 0, "stock": 12, "sales": 10},
    {"itemId": 7, "shopId": 3, "shopName": "Emmas Business", "itemName": "Bin Chicken", "liveOrders": 0, "stock": 30, "sales": 10},
    {"itemId": 8, "shopId": 3, "shopName": "Emmas Business", "itemName": "Christmas Giraffe", "liveOrders": 0, "stock": 8, "sales": 15},
    {"itemId": 9, "shopId": 3, "shopName": "Emmas Business", "itemName": "Elephant Sticker", "liveOrders": 0, "stock": 10, "sales": 12},
]

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/listing')
def get_listings():
    return jsonify(listings)

@app.route('/businesses/<int:shopId>/listings')
def get_listings_by_shopId(shopId):
    listings_with_shopId = [listing for listing in listings if listing['shopId'] == shopId]
    return jsonify(listings_with_shopId)
