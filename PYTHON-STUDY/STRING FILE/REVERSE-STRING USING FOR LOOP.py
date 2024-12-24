String = input("ENTER ANY WORD (OR) SENTENCE: ")
Reverse_string = ""
for i in range(len(String) - 1,-1,-1):
  Reverse_string += String[i]
print("THE REVERSE OF THE WORD (OR) SENTENCE IS: ",Reverse_string)  
