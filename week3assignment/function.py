
def calculate_discount(price, discount_percent):
    if discount_percent >= 20: 
        discount = (discount_percent / 100) * price 
        discounted_price = price - discount
        return discounted_price
    else:
        return price
   

    #getting user input
price = float(input("Enter the price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))
final_price = calculate_discount(price, discount_percent)

    #output the final price
print("The final price after discount is:", final_price)


    
