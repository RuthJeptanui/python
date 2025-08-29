# Assignment: Object-Oriented Programming in Python 🐍

This project demonstrates **OOP concepts** such as:
- Classes & Objects
- Constructors
- Inheritance
- Polymorphism

---

## 📘 Assignment 1: Custom Class

We created a **Smartphone** class that inherits from a **Device** class.

### Features:
- Attributes: brand, model, storage, camera megapixels
- Methods:
  - `device_info()` → shows device brand & model
  - `take_photo()` → simulates taking a photo
  - `storage_info()` → shows available storage

### Example:
```python
phone1 = Smartphone("Samsung", "Galaxy S23", 256, 50)
print(phone1.device_info())    
print(phone1.take_photo())      
