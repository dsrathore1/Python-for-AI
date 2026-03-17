class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Ruby", "Beagle")

print("Name of dog :-> ", dog1.name)
print("Breed of dog :-> ", dog2.breed)


class Cat:
    def __init__(self, name):
        self.name = name


cat1 = Cat("Uno")
cat2 = Cat(name="Kitty")

print(cat1.name)
print(cat2.name)