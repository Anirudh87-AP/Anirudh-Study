a = int(input("a:"))
b = int(input("b:"))
c_ODD = 0
c_EVEN =0
for i in range(a,b+1):
  if i%2 == 1:
    c_ODD += 1
  else: #i%2 == 0
    c_EVEN += 1
print("NO OF ODD NUMBER BETWEEN a AND b IS: ",c_ODD)
print("NO OF EVEN NUMBER BETWEEN a AND b IS: ",c_EVEN)
