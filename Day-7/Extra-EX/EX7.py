class MenuItem:
    def __init__(self, name, price, category): 
        self.name = name
        self.price = price
        self.category = category

    def display(self):
        return self.name + " (" + self.category + ") - $" + str(round(self.price, 2))


class Order:
    def __init__(self): 
        self.items = []  

    def add_item(self, item):
        self.items.append(item)
        print("Added:", item.name)

    def remove_item(self, name):
        for i in range(len(self.items)):
            if self.items[i].name.lower() == name.lower():
                removed = self.items.pop(i)
                print("Removed:", removed.name)
                return
        print("Item not found:", name)

    def calculate_total(self):
        total = 0
        for it in self.items:
            total = total + it.price
        return total

    def display_order(self):
        if len(self.items) == 0:
            print("Order is empty.")
            return
        print("Your order:")
        for it in self.items:
            print("-", it.display())
        print("Total: " + str(round(self.calculate_total(), 2)))


burger = MenuItem("Burger", 4.5, "Main")
fries = MenuItem("Fries", 1.5, "Side")
cola = MenuItem("Cola", 1.25, "Drink")

order = Order()
order.add_item(burger)
order.add_item(fries)
order.add_item(cola)

order.display_order()

order.remove_item("Fries")