products = [
    {"name": "Apple", "price": 25},
    {"name": "Banana", "price": 30},
    {"name": "Cucumber", "price": 15},
    {"name": "Orange", "price": 40}
]

def total_price(products):
    total = 0
    for product in products:
        total += product["price"]
    return total

result = total_price(products)
print(f"Total: {result}")