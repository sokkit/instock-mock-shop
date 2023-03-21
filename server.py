from flask import Flask, jsonify, request

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

@app.route('/listings', methods=['POST'])
def add_listing():
    new_listing = request.get_json()
    new_listing['itemId'] = len(listings) + 1 
    listings.append(new_listing)
    return jsonify({'message': 'Listing added successfully', 'listing': new_listing}), 201

@app.route('/listings/<int:item_id>', methods=['GET'])
def get_listing(item_id):
    listing = next((listing for listing in listings if listing['itemId'] == item_id), None)
    if listing:
        return jsonify(listing)
    else:
        return jsonify({'message': 'Item not found'}), 404

@app.route('/listings/<int:item_id>/live-orders', methods=['PUT'])
def update_listing_live_orders(item_id):
    # Get the request body data
    data = request.get_json()
    # Find the listing with the given item ID
    listing = next((listing for listing in listings if listing['itemId'] == item_id), None)
    if listing is not None:
        # Update the listing's liveOrders value
        listing['liveOrders'] = data['liveOrders']
        return jsonify({'message': 'Listing updated successfully.'}), 200
    else:
        return jsonify({'message': 'Listing not found.'}), 404

@app.route('/listings/<int:item_id>/sales', methods=['PUT'])
def update_listing_sales(item_id):
    # Get the request body data
    data = request.get_json()
    # Find the listing with the given item ID
    listing = next((listing for listing in listings if listing['itemId'] == item_id), None)
    if listing is not None:
        # Update the listing's sales value
        listing['sales'] = data['sales']
        return jsonify({'message': 'Listing updated successfully.'}), 200
    else:
        return jsonify({'message': 'Listing not found.'}), 404