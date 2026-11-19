from flask import Flask, request, jsonify
import requests


app = Flask(__name__)

# Temporary inventory database
inventory = [
    {
        "id": 1,
        "name": "Milk",
        "category": "Beverages",
        "quantity": 50,
        "price": 100
    },
    {
        "id": 2,
        "name": "Doughnuts",
        "category": "Bakery",
        "quantity": 30,
        "price": 60
    }
]

def get_product(barcode):
    url = f"https://world.openfoodfacts.org/api/v2/product/{barcode}.json"

    headers = {
        "User-Agent": "InventoryManagementApp/1.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)

        print("Status code:", response.status_code)

        data = response.json()

        if data.get("status") == 1:
            return data["product"]

        return None

    except requests.RequestException as error:
        print("API error:", error)
        return None

@app.route("/")
def home():
    return "<h1>Welcome to inventory management system!</h1>"

# 1. GET - Fetch all inventory items
@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(inventory), 200


# 2. GET - Fetch a single inventory item
@app.route("/inventory/<int:id>", methods=["GET"])
def get_item(id):
    for item in inventory:
        if item["id"] == id:
            return jsonify(item), 200

    return jsonify({"error": "Item not found"}), 404


# 3. POST - Add a new inventory item
@app.route("/inventory", methods=["POST"])
def add_item():
    data = request.get_json()

    barcode = data["barcode"]

    product = get_product(barcode)

    if product is None:
        return jsonify({"error": "Product not found"}), 404

    new_item = {
        "id": len(inventory) + 1,
        "name": product.get("product_name", ""),
        "brand": product.get("brands", ""),
        "ingredients": product.get("ingredients_text", ""),
        "barcode": barcode,
        "quantity": data.get("quantity", 0),
        "price": data.get("price", 0)
    }

    inventory.append(new_item)

    return jsonify(new_item), 201


# 4. PATCH - Update an existing inventory item
@app.route("/inventory/<int:id>", methods=["PATCH"])
def update_item(id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    for item in inventory:
        if item["id"] == id:

            item.update(data)

            return jsonify({
                "message": "Item updated successfully",
                "item": item
            }), 200

    return jsonify({"error": "Item not found"}), 404


# 5. DELETE - Remove an inventory item
@app.route("/inventory/<int:id>", methods=["DELETE"])
def delete_item(id):
    for item in inventory:
        if item["id"] == id:

            inventory.remove(item)

            return jsonify({
                "message": "Item deleted successfully"
            }), 200

    return jsonify({"error": "Item not found"}), 404

@app.route("/products/<barcode>", methods=["GET"])
def find_product(barcode):
    product = get_product(barcode)

    if product is None:
        return jsonify({"error": "Product not found or API unavailable"}), 404

    return jsonify(product), 200


if __name__ == "__main__":
    app.run(debug=True)
