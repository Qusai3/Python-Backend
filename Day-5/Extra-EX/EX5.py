inventory = {
    "apple": {"price": 1.5, "category": "fruit"},
    "banana": {"price": 0.75, "category": "fruit"},
    "milk": {"price": 2.99, "category": "dairy"},
    "bread": {"price": 3.25, "category": "bakery"},
    "cheese": {"price": 4.5, "category": "dairy"},
    "chocolate": {"price": 2.25, "category": "snacks"}
}

cart = ["apple", "banana", "milk", "cheese", "chocolate"]


total_price = 0
unique_categories = set()
most_expensive_item = ""
highest_price = 0

for item in cart:
    if item in inventory:
        if (price := inventory[item]["price"]) > highest_price:
            highest_price = price
            most_expensive_item = item

        total_price += price
        unique_categories.add(inventory[item]["category"])

print("RECEIPT")
for item in cart:
    price = inventory[item]["price"]
    category = inventory[item]["category"]
    print(f"{item.title():<10} - ${price:.2f} [{category}]")

print(f"Total: ${total_price:.2f}")
print(f"Unique categories: {unique_categories}")
print(f"Most expensive item: {most_expensive_item.title()} (${highest_price:.2f})")