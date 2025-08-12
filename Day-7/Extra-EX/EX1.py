print("EX1")
class Person:
    def __init__(self, name, age): 
        self.name = name
        self.age = age

    def introduce(self):
        return "Hello, my name is " + self.name + " and I am " + str(self.age) + " years old."


p1 = Person("Qusai", 23)
p2 = Person("Omar",22)

print(p1.introduce())
print(p2.introduce())