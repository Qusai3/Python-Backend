class Product:
    def __init__(self, product_id, name, price, quantity=0): 
        self.product_id = product_id
        self.name = name
        self.price = price     
        self.quantity = quantity

    def apply_discount(self, percent):
        if percent < 0:
            print("Percent must be positive.")
            return
        discount_amount = (percent / 100.0) * self.price
        self.price = self.price - discount_amount

    def restock(self, amount):
        if amount > 0:
            self.quantity += amount
        else:
            print("Restock amount must be positive.")

    def _get_price(self):
        return self.price

    def _set_price(self, value):
        self.price = value

    def __add__(self, other): 
        if type(self) is not type(other):
            raise ValueError("Can only add products of the same type.")
        if self.product_id != other.product_id:
            raise ValueError("Product IDs must match to combine quantities.")
        return self._combine_like(other)

    def __call__(self):  
        return f"{self.name} (ID: {self.product_id}) - ${self._get_price():.2f} x {self.quantity}"

    def _combine_like(self, other):
        
        new_obj = Product(self.product_id, self.name, self._get_price(), self.quantity + other.quantity)
        return new_obj

    def __str__(self):  
        return self.__call__()


class DigitalProduct(Product):
    def __init__(self, product_id, name, price, quantity=0, file_size=0):  
        super().__init__(product_id, name, price, quantity)
        self.file_size = file_size  # MB

    
    def apply_discount(self, percent):
        if percent > 20:
            percent = 20
        super().apply_discount(percent)

    def _combine_like(self, other):
        if self.file_size != other.file_size:
            raise ValueError("Digital products must have the same file size to combine.")
        return DigitalProduct(self.product_id, self.name, self._get_price(),
                              self.quantity + other.quantity, self.file_size)


class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, quantity=0, weight=0):
        super().__init__(product_id, name, price, quantity)
        self.weight = weight  

    
    def apply_discount(self, percent):
        old = self._get_price()
        super().apply_discount(percent)
        if self._get_price() < 5:
            self._set_price(5)
        if self._get_price() != old and self._get_price() == 5:
            print("Price clamped to minimum $5.")

    def _combine_like(self, other):
        if self.weight != other.weight:
            raise ValueError("Physical products must have the same weight to combine.")
        return PhysicalProduct(self.product_id, self.name, self._get_price(),
                               self.quantity + other.quantity, self.weight)


dp1 = DigitalProduct("D101", "Photo Pack", 20, 3, file_size=500)
dp2 = DigitalProduct("D101", "Photo Pack", 20, 2, file_size=500)

print(dp1())           
print(dp2())

dp1.apply_discount(50)  
print("After discount:", dp1())

combined_dp = dp1 + dp2
print("Combined:", combined_dp())

pp1 = PhysicalProduct("P501", "Mug", 7, 5, weight=0.3)
pp1.apply_discount(40)  