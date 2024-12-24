n = int(input("ENTER THE NUMBER OF ROWS/COLOUMS OF THE PYRAMID: "))
for i in range(1, n + 1):
  for j in range(1, i + 1):
    print("*", end = " ")
  print()
for i in range(n - 1, 0, -1):
  for j in range(1, i + 1):
    print("*", end = " ")
  print()
  
