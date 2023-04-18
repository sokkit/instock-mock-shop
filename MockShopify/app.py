from flask import Flask, jsonify, request
import secrets
import string

print("running")

listings = [
    {"itemId": 1, "shopId": 1, "shopName": "Johns Business",
        "itemName": "Birthday Cockatoo", "liveOrders": 3, "stock": 20, "sales": 32},
    {"itemId": 2, "shopId": 1, "shopName": "Johns Business",
        "itemName": "Blank Koala", "liveOrders": 4, "stock": 15, "sales": 31},
    {"itemId": 3, "shopId": 1, "shopName": "Johns Business",
        "itemName": "Birthday Crocodile", "liveOrders": 6, "stock": 40, "sales": 16},
    {"itemId": 4, "shopId": 2, "shopName": "TillyScribbles",
        "itemName": "Nestle Pure Life", "liveOrders": 7, "stock": 18, "sales": 30},
    {"itemId": 5, "shopId": 2, "shopName": "TillyScribbles",
        "itemName": "Birthday LLama", "liveOrders": 1, "stock": 19, "sales": 22},
    {"itemId": 6, "shopId": 2, "shopName": "TillyScribbles",
        "itemName": "Magic Avocado", "liveOrders": 2, "stock": 22, "sales": 18},
    {"itemId": 7, "shopId": 3, "shopName": "Emmas Business",
        "itemName": "Bin Chicken", "liveOrders": 3, "stock": 40, "sales": 10},
    {"itemId": 8, "shopId": 3, "shopName": "Emmas Business",
        "itemName": "Christmas Giraffe", "liveOrders": 4, "stock": 12, "sales": 11},
    {"itemId": 9, "shopId": 3, "shopName": "Emmas Business",
        "itemName": "Elephant Sticker", "liveOrders": 5, "stock": 15, "sales": 17},
]

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>InStock Mock Shop</p>"

# Generated using ChatGPT
# Prompt given
# Can you create an endpoint that lets users login by sending a shopname that is within the listings and a password of "Password123"
# and returns a mock auth token if the login is successful


@app.route('/authenticate', methods=['POST'])
def authenticate():
    data = request.get_json()

    if 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Missing username or password'}), 400

    shop_name = data['username']
    password = data['password']

    if any(listing['shopName'] == shop_name for listing in listings) and password == "Password123":
        # User is logged in, generate an authentication token
        token = ''.join(secrets.choice(string.ascii_letters +
                        string.digits) for _ in range(64))

        return jsonify({'message': 'Login successful', 'shopName': shop_name, 'authToken': token}), 200
    else:
        return jsonify({'message': 'Invalid shopName or password'}), 401


@app.route('/listings')
def get_listings():
    return jsonify(listings)


@app.route('/businesses/<int:shopId>/listings')
def get_listings_by_shopId(shopId):
    listings_with_shopId = [
        listing for listing in listings if listing['shopId'] == shopId]
    return jsonify(listings_with_shopId)


@app.route('/listings', methods=['POST'])
def add_listing():
    new_listing = request.get_json()
    new_listing['itemId'] = len(listings) + 1
    listings.append(new_listing)
    return jsonify({'message': 'Listing added successfully', 'listing': new_listing}), 201


@app.route('/listings/<int:item_id>', methods=['GET'])
def get_listing(item_id):
    listing = next(
        (listing for listing in listings if listing['itemId'] == item_id), None)
    if listing:
        return jsonify(listing)
    else:
        return jsonify({'message': 'Item not found'}), 404


@app.route('/listings/<int:item_id>/live-orders', methods=['PUT'])
def update_listing_live_orders(item_id):
    data = request.get_json()
    listing = next(
        (listing for listing in listings if listing['itemId'] == item_id), None)
    if listing is not None:
        listing['liveOrders'] = data['liveOrders']
        return jsonify({'message': 'Listing updated successfully.'}), 200
    else:
        return jsonify({'message': 'Listing not found.'}), 404


@app.route('/listings/<int:item_id>/sales', methods=['PUT'])
def update_listing_sales(item_id):
    data = request.get_json()
    listing = next(
        (listing for listing in listings if listing['itemId'] == item_id), None)
    if listing is not None:
        listing['sales'] = data['sales']
        return jsonify({'message': 'Listing updated successfully.'}), 200
    else:
        return jsonify({'message': 'Listing not found.'}), 404


@app.route('/listings/<int:item_id>/stock', methods=['PUT'])
def update_listing_stock(item_id):
    data = request.get_json()
    listing = next(
        (listing for listing in listings if listing['itemId'] == item_id), None)
    if listing is not None:
        listing['stock'] = data['stock']
        return jsonify({'message': 'Listing updated successfully.'}), 200
    else:
        return jsonify({'message': 'Listing not found.'}), 404
