rows  = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
matrix = []
for i in range(rows):
  a = []
  for j in range(columns):
      v = int(input(f"Enter the Matrix[{i + 1}{j + 1}] element of a Matrix: "))
      a.append(v)
  matrix.append(a)
for i in range(rows):
  for j in range(columns):
    print(matrix[i][j],end = " ")
  print()
def u(Matrix,Rows,Columns):
  for i in range(Rows):
    for j in range(Columns):
      if i > j:
        print("0", end = " ")
      else:
        print(Matrix[i][j], end = " ")
    print()
print("The upper triangular matrix is: ")
u(matrix,rows,columns)
def l(Matrix,Rows,Columns):
  for i in range(Rows):
    for j in range(Columns):
      if i < j:
        print("0", end = " ")
      else:
        print(Matrix[i][j], end = " ")
    print()
print("The lower triangular matrix is: ")
l(matrix,rows,columns)
