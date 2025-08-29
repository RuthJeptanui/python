# Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"{self.brand} {self.model}"

# Child class (inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, camera_megapixels):
        super().__init__(brand, model)  
        self.storage = storage
        self.camera_megapixels = camera_megapixels
    
    def take_photo(self):
        return f"Photo from {self.camera_megapixels} MP camera."
    
    def storage_info(self):
        return f"Checkout my storage at: {self.storage} GB"

# Create objects
phone1 = Smartphone("Samsung", "Galaxy S23", 256, 50)
phone2 = Smartphone("Apple", "iPhone 14", 128, 48)

# Use methods
print(phone1.device_info())
print(phone1.take_photo())
print(phone1.storage_info())

print(phone2.device_info())
print(phone2.take_photo())
print(phone2.storage_info())


#question 2

class Vehicle:
    def move(self):
        pass  

class Car(Vehicle):
    def move(self):
        return "is on the road"

class Plane(Vehicle):
    def move(self):
        return "up in the sky"

class Boat(Vehicle):
    def move(self):
        return "submerged in water"

# polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v.move())

