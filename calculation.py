#input
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
operation = input("+, /, -, *")

#conditions  for performing the arithmetics
if operation == "+" :
 results = num1 + num2
 print(f"{num1} + {num2} = {results}")
elif operation == "-" :
 results = num1 - num2
 print(f"{num1} - {num2} = {results}")
elif operation == "*":
 results = num1 * num2
 print(f"{num1} * {num2} = {results}")
elif operation == "/":
 if num2 != 0:
  results = num1 / num2
  print(f"{num1} / {num2} = {results}")
 else :
  print("Error, 0 is not allowed in division ")
else:
 print("wrong operation")