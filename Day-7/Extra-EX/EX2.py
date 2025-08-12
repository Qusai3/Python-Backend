class Dog:
    species = "Canis familiaris"  

    def __init__(self, name, breed):  
        self.name = name
        self.breed = breed

    def describe(self):
        return self.name + " is a " + self.breed + ". Species: " + Dog.species


d1 = Dog("Bobby", "Retriever")
d2 = Dog("Maxz", "Bulldog")

print(d1.describe())
print(d2.describe())

Dog.species = "Wolf"
print(d1.describe())
print(d2.describe())

d1.species = "Alien Dog"
print(d1.species)  
print(d2.species)  