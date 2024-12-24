a = int(input("Enter the Integer a: "))
b = int(input("Enter the Integer b: "))
c = int(input("Enter the Integer c: "))
print(f"The relation between (a: {a} , b: {b} , c: {c}) is: ")
if a > b:
  if b > c:
    print(f"a: {a} > b: {b} > c: {c}")
  elif b < c:
    if a > c:
      print(f"a: {a} > c: {c} > b: {b}")
    elif a < c:
      print(f"c: {c} > a: {a} > b: {b}")
    else: # a == c
      print(f"( a: {a} = c: {c} ) > b: {b}")
  else: # b == c
    print(f"a: {a} > ( b: {b} = c: {c} )")
elif a < b:
  if a > c:
    print(f"b: {b} > a: {a} > c: {c}")
  elif a < c:
    if b > c:
      print(f"b: {b} > c: {c} > a: {a}")
    elif b < c:
      print(f"c: {c} > b: {b} > a: {a}")
    else: # b == c
      print(f"( b: {b} = c: {c} ) > a: {a}")
  else: # a == c
    print(f"b: {b} > ( a: {a} = c: {c} )")
else: # a == b
  if a > c:
    print(f" ( a: {a} = b: {b} ) > c: {c}")
  elif a < c:
    print(f"c: {c} > ( a: {a} = b: {b} )")
  else: # a == c
    print(f"( a: {a} = b: {b} = c: {c} )")
