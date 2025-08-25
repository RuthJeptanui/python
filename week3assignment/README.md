# 📘 Calculate Discount

This is a simple Python program that calculates the final price of an item after applying a discount.
If the discount percentage is **20% or higher**, the discount is applied. Otherwise, the original price is returned.

---

## 🚀 Features

* Takes the original price of an item.
* Takes the discount percentage.
* Applies the discount **only if it is 20% or more**.
* Returns the final price or the original price.

---

## 📝 Function Description

```python
def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    If discount is 20% or higher, apply it.
    Otherwise, return the original price.
    """
```

**Parameters**:

* `price` (float): Original price of the item.
* `discount_percent` (float): Discount percentage to apply.

**Returns**:

* `float`: Final price after applying discount, or original price if discount < 20%.

---

## ▶️ How to Run

1. Clone or download this repository.
2. Run the Python file in your terminal:

   ```bash
   python discount.py
   ```
3. Enter the original price and discount percentage when prompted.

---

## 💻 Example Run

```
Enter the original price: 1000
Enter the discount percentage: 25
The final price is: 750.00
```

```
Enter the original price: 500
Enter the discount percentage: 15
The final price is: 500.00
```

---

## 📂 Project Structure

```
.
├── discount.py   # Main Python program
└── README.md               # Project documentation
```

