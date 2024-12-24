n = int(input("ENTER THE NUMBER OF ELEMENT IN LIST: "))
List  = []
for i in range(1,n + 1):
  if i == 1:
    List.append(int(input("ENTER THE 1st ELEMENT OF THE LIST: ")))
  elif i == 2:
    List.append(int(input("ENTER THE 2nd ELEMENT OF THE LIST: ")))
  elif i == 3:
    List.append(int(input("ENTER THE 3rd ELEMENT OF THE LIST: ")))
  else: # i > 3
    List.append(int(input(f"ENTER THE {i} ELEMENT OF THE LIST: ")))    
print(f"THEN THE LIST IS: {List}")  
Max_num = Min_num = List[0]
for Num in List:
  if Num > Max_num:
    Max_num = Num
  elif Num < Min_num:
    Min_num = Num
if Max_num == Min_num:
  print("THERE IS NO MAXIMUM OR MINIMUM NUMBER IN THE LIST") 
else:
  print("THE MAXIMUM NUMBER IS: ", Max_num)
  print("THE MINIMUM NUMBER IS: ", Min_num)
