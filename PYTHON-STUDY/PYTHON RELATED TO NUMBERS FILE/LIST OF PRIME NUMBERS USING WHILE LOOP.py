n = int(input("Enter the Number,Upto which you want to form a list for Prime Numbers: "))
Numbers = []
Prime_Numbers = []
for i in range(1,n + 1):
  Numbers.append(i)
print(f"The List of Numbers from 1 to {n} is: ",Numbers)
j = 2
while j <= n:
  Is_Prime = True
  for k in range(2,j):
    if j % k == 0:
      Is_Prime = False
      break
  if Is_Prime:
    Prime_Numbers.append(j)
  j += 1
print(f"The List of Prime Numbers from 1 to {n} is: ",Prime_Numbers)
