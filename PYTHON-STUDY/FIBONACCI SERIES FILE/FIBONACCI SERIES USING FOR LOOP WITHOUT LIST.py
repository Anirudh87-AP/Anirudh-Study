n = int(input("ENTER THE NUMBER OF TERMS IN FIBONACCI SEQUENCE: "))
print("ENTER THE FIRST TWO NUMBERS a AND b OF FIBONACCI SEQUENCE: ")
a = int(input("a = "))
b = int(input("b = "))
c = 0
print(f"THE FIBONACCI SEQUENCE STARTING WITH {a} AND {b} UPTO {n} TERMS IS: ")
print(a, b, end = " ")
for i in range(1, n - 1):
  c = a + b
  print(c, end=" ")
  a = b
  b = c
