import requests

BASE_URL = "http://127.0.0.1:5000/products"

# Add a new product
def add_product(name, description, price):
    payload = {'name': name, 'description': description, 'price': price}
    response = requests.post(BASE_URL, json=payload)
    if response.status_code == 201:
        print("Product created:", response.json())
    else:
        print("Error:", response.json())

# Retrieve all products
def get_all_products():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        print("Products:", response.json())
    else:
        print("Error:", response.json())

# Test the script
if __name__ == '__main__':
    # Add sample products
    add_product("Laptop", "A high-performance laptop", 1500.99)
    add_product("Phone", "A flagship smartphone", 799.49)

    # Retrieve all products
    get_all_products()
