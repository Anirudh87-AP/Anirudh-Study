n = int(input("ENTER THE NUMBERS TERMS IN FIBONACCI SEQUENCE: "))
print("ENTER THE FIRST TWO NUMBERS a AND b OF FIBONACCI SEQUENCE: ")
a = int(input("a = "))
b = int(input("b = "))
List = [a, b]
for i in range(2, n):
  Next_Number = List[i - 1] + List[i - 2]
  List.append(Next_Number)
print(f"THE LIST OF FIBONACCI SEQUENCE STARTING FROM {a} AND {b} UPTO {n} IS: ")
print(List)
