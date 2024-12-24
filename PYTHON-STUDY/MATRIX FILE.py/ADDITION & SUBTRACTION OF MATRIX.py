Rows = int(input("Enter the number of Rows of Matrix a & b: "))
Columns = int(input("Enter the number of Columns of Matrix a & b: "))
a = []
b = []
print("Enter the elements of Matrix a: ")
for i in range(Rows):
  c = []
  for j in range(Columns):
    v = int(input(f"Enter the a[{i + 1}{j + 1}] element of Matrix a: "))
    c.append(v)
  a.append(c)
print("Enter the elements of Matrix b: ")
for i in range(Rows):
  c = []
  for j in range(Columns):
    v = int(input(f"Enter the b[{i + 1}{j + 1}] element of Matrix b: "))
    c.append(v)
  b.append(c)
print("The Matrix a & b are: ")
print("Matrix a: ")
for i in range(Rows):
  for j in range(Columns):
    print(a[i][j], end = " ")
  print()
print("Matrix b: ")
for i in range(Rows):
  for j in range(Columns):
    print(b[i][j], end = " ")
  print()
Matrix_1 = [ [0,0,0],
           [0,0,0],
           [0,0,0] ]
Matrix_2 = [ [0,0,0],
             [0,0,0],
             [0,0,0] ]
for i in range(len(a)):
  for  j in range(len(b)):
    Matrix_1[i][j] = a[i][j] + b[i][j]
print("The Addition of Matrix a & b is: ")
for i in range(len(a)):
  for j in range(len(b)):
    print(Matrix_1[i][j], end = " ")
  print()
for i in range(len(a)):
  for  j in range(len(b)):
    Matrix_2[i][j] = a[i][j] - b[i][j]
print("The Subtraction of Matrix a & b is : ")
for i in range(len(a)):
  for j in range(len(b)):
    print(Matrix_2[i][j], end = " ")
  print()
