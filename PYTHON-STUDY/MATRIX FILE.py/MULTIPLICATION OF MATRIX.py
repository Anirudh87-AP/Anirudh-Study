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
Matrix = [[0 for _ in range(Columns)] for _ in range(Rows)]
for i in range(len(a)):
  for j in range(len(b[0])):
    for k in range(len(b)):
      Matrix[i][j] += a[i][k] * b[k][j]
print("The Multiplication of Matrix a & b is: ")
for i in range(len(Matrix)):
  for j in range(len(Matrix[0])):
    print(Matrix[i][j], end = " ")
  print()
