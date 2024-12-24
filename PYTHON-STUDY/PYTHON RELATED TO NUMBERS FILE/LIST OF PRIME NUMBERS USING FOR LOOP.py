n = int(input("Enter the Number,Upto which you want to form a List for Prime Numbers: "))
Numbers = []
Prime_Numbers = []
for i in range(1, n + 1):
  Numbers.append(i)
print(f"The List of Numbers from 1 to {n} is: ",Numbers)
for j in Numbers:
  if j == 1:
    continue
  elif j == 2:
    Prime_Numbers.append(j)
  else:
    for k in range(2, j):
      if j % k == 0:
        break
    else:
      Prime_Numbers.append(j)
print(f"The List of Prime Numbers from 1 to {n} is: ", Prime_Numbers)
