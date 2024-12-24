def calculate_grade(PERCENTAGE):
  """Calculates and returns the grade based on the percentage."""
  if PERCENTAGE >= 90:
    return "A1"
  elif 80 <= PERCENTAGE < 90:
    return "A2"
  elif 70 <= PERCENTAGE < 80:
    return "B1"
  elif 60 <= PERCENTAGE < 70:
    return "B2"
  elif 50 <= PERCENTAGE < 60:
    return "C1"
  elif 40 <= PERCENTAGE < 50:
    return "C2"
  elif 30 <= PERCENTAGE < 40:
    return "E" 
  else: #PERCENTAGE < 30
    return "F"
def display_mark_sheet(student_data):
  """Prints a formatted mark sheet for the given student data."""
  print("-" * 40)
  print("Student Mark Sheet")
  print("-" * 40)
  print(f"Student Name: {student_data['Name']}")
  print(f"Subject: {student_data['Subject']}")
  print(f"Marks Scored: {student_data['Marks']}")
  print(f"PERCENTAGE: {student_data['Percentage']:.2f}%")
  print(f"Grade: {student_data['Grade']}")
  print("-" * 40)
def get_student_data():
  """Prompts the user to enter student information and returns it."""
  NAME = input("ENTER THE STUDENT'S NAME: ")
  SUBJECT = input("ENTER THE SUBJECT'S NAME: ")
  while True:
    try:
      MARKS = int(input("ENTER THE MARK SCORED (OUT OF 80): "))
      if 0 <= MARKS <= 80:
        break
      else:
        print("Invalid marks. Please enter a value between 0 and 80.")
    except ValueError:
      print("Invalid input. Please enter a number.")
  PERCENTAGE= (MARKS / 80) * 100
  GRADE = calculate_grade(PERCENTAGE)
  return {
    'Name': NAME,
    'Subject': SUBJECT,
    'Marks': MARKS,
    'Percentage': PERCENTAGE,
    'Grade': GRADE
  }
if __name__ == "__main__":
  student_data = get_student_data()
  display_mark_sheet(student_data)
