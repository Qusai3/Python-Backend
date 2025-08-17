class Circle:
    def __init__(self, radius):  # Fixed constructor name
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle:
    def __init__(self, length, width):  # Fixed constructor name
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


c = Circle(5)
print("Circle area:", c.area())
print("Circle perimeter:", c.perimeter())

r = Rectangle(4, 6) 
print("Rectangle area:", r.area())
print("Rectangle perimeter:", r.perimeter())