n = int(input("ENTER THE TABLE YOU WANT: "))
m = int(input("ENTER THE NUMBER OF ROWS YOU WANT: "))
print(f"TABLE OF {n} IS: ")
for i in range(1,m + 1):
  print(n,'x',i,'=',i*n)
