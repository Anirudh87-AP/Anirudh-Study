print("ENTER THE VALUES OF a AND b: ")
a = int(input("a = "))
b = int(input("b = "))
print("CHOOSE A OPERATION: ")
print("1. ADDITION")
print("2. SUBTRACTION")
print("3. MULTIPLICATION")
print("4. DIVISION")
while True:
  Choice = input("ENTER YOUR CHOICE (1/2/3/4): ")
  if Choice in ('1', '2', '3', '4'):
    break
  else:
    print("INVALID INPUT. PLEASE ENTER NUMBER BETWEEN 1 and 4.")
if Choice == '1':
  print("THE SUM OF a AND b IS: ", a + b)
elif Choice == '2':
  print("THE DIFFERENCE OF a AND b IS: ", a - b)
elif Choice == '3':
  print("THE PRODUCT OF a AND b IS: ", a * b)
elif Choice == '4':
  print("THE DIVISION OF a AND b IS: ", a / b)
