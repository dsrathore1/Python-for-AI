#! Inheritence (genetics)
# ? Create an Electric car class that inherits from the Car class and has an additional attribute battery_size


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fullName(self):
        return f"Brand : {self.brand}\nModel : {self.model}"

    def fuelType(self):
        return "Petrol & Diesel"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuelType(self):
        return "Electric Charges!"


my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

print("Brand name : ", my_tesla.brand)
print(my_tesla.fullName())


#! Polymorphism (Anek roop)
# ? Demonstrate polymorphism by defining a method fuel_type in both Car & Electric car classes,but with different behaviour.

my_byd = ElectricCar("BYD", "Model X", "90kWh")
print(f"\nFuel Type of {my_byd.brand} : ", my_byd.fuelType())

my_safari = Car("Tata", "Safari")
print(f"Fuel Type of {my_safari.model} : ", my_safari.fuelType())


#! Encapsulation (private karna)
# ? Modify the car class to encapsule the brand attribute, making it private and provide it getter method for it.


class Pet:
    def __init__(self, name, breed):
        self.__name = name  # * Private the attribute
        self.breed = breed

    def get_name(self) -> str:
        return self.__name + "!"  # * It is only accessible inside own class.


class Dog(Pet):
    def __init__(self, name, breed, size):
        super().__init__(name, breed)
        self.size = size

    def definePet(self):
        return f"Name: {self.get_name()}\nBreed : {self.breed}\nSize : {self.size}"


my_dog = Dog("Max", "German Shepered", "short")
# print(my_dog.__name) # You can't directly access this attribute anymore now.
print("\nName of dog : ", my_dog.get_name())
print("\nPet :\n", my_dog.definePet())
