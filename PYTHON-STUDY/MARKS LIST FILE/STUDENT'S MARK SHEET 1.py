MS = int(input("ENTER YOUR MARK SCORED (/80):"))
P = (MS/80)*100
if MS >= 35:
  print("YOU PASSED THE EXAM WITH:", P ,"%")
  if P >= 90:
    print("YOUR GRADE IS: A1 ")
  elif (80 <= P < 90):
    print("YOUR GRADE IS: A2 ")
  elif (70 <= P < 80):
    print("YOUR GRADE IS: B1 ")
  elif (60 <= P < 70):
    print("YOUR GRADE IS: B2 ")
  elif (50 <= P < 60):
    print("YOUR GRADE IS: C1 ")
  elif (40 <= P < 50):
    print("YOUR GRADE IS: C2 ")
  else:  #P <= 40
    print("YOUR GRADE IS: D ")
else:
  if (30 <= MS < 35):
    print("YOU HAVE FAILED IN EXAM WITH GRADE: E ")
    print("NEXT TIME TRY TO GET PASS MARK")
  else: #MS < 30
    print("YOU FAILED IN EXAM WITH GRADE: F ")
    print("VERY POOR GRADE YOU MUST STUDY HARD")
