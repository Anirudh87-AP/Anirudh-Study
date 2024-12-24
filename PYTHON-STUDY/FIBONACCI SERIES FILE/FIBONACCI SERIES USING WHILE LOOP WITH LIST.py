n = int(input("ENTER THE NUMBER OF TERMS IN FIBONACCI SEQUENCE: "))
print("ENTER THE FIRST TWO NUMBERS OF FIBONACCI SEQUENCE a AND b: ")
a = int(input("a = "))
b = int(input("b = "))
List = [a,b]
Next_Number = 0 
i = 2
while i in range(2,n):
  Next_Number = List[i-1] + List[i-2]
  List.append(Next_Number)
  i += 1
print(f"THE LIST OF FIBONACCI SEQUENCE STARTING WITH {a} AND {b} UPTO {n} TERMS IS: ")
print(List)
