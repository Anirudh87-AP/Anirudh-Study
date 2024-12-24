n = int(input("ENTER THE NUMBER OF ROWS/COLOUMS OF THE PYRAMID: "))
for i in range(n, 0, -1):
  print(" " * (n - i) * 2, end = " ")
  for j in range(i, 0, -1):
    print("*", end = " ")
  print()
